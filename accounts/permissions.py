from functools import wraps

from django.contrib import messages
from django.shortcuts import redirect

from .models import Modulo, Permissao


# =====================================================
# VERIFICAR PERMISSÃO
# =====================================================

def tem_permissao(usuario, codigo_modulo, acao="visualizar"):

    print("=" * 60)
    print("USUÁRIO:", usuario.username)
    print("MÓDULO:", codigo_modulo)
    print("AÇÃO:", acao)

    if not usuario.is_authenticated:
        print("Usuário não autenticado")
        return False

    if usuario.is_superuser:
        print("Superusuário")
        return True

    if not hasattr(usuario, "perfil"):
        print("Sem perfil")
        return False

    perfil = usuario.perfil.perfil_acesso

    if perfil is None:
        print("Perfil inexistente")
        return False

    print("PERFIL:", perfil.nome)

    if perfil.nome == "Administrador":
        print("Administrador")
        return True

    try:

        modulo = Modulo.objects.get(
            codigo=codigo_modulo.lower(),
            ativo=True
        )

        print("MÓDULO ENCONTRADO:", modulo.codigo)

    except Modulo.DoesNotExist:

        print("MÓDULO NÃO ENCONTRADO")

        return False

    try:

        permissao = Permissao.objects.get(
            perfil=perfil,
            modulo=modulo
        )

        print("PERMISSÃO ENCONTRADA")

    except Permissao.DoesNotExist:

        print("PERMISSÃO NÃO ENCONTRADA")

        return False

    print("VALOR:", getattr(permissao, acao, "AÇÃO INVÁLIDA"))

    return getattr(permissao, acao)

# =====================================================
# ESCOPO DOS DADOS
# =====================================================

def filtrar_escopo(usuario, queryset):

    # Superusuário vê tudo
    if usuario.is_superuser:
        return queryset

    # Usuário sem perfil
    if not hasattr(usuario, "perfil"):
        return queryset.none()

    perfil = usuario.perfil.perfil_acesso

    if perfil is None:
        return queryset.none()

    # Perfis com acesso total
    if perfil.nome in [
        "Administrador",
        "Gestor",
        "Secretária",
        "Contabilidade",
        "Auditoria",
    ]:
        return queryset

    # Dentista
    if perfil.nome == "Dentista":

        if hasattr(queryset.model, "paciente"):
            return queryset.filter(
                paciente__dentista=usuario
            )

        return queryset

    # Auxiliar de Saúde Bucal
    if perfil.nome == "Auxiliar de Saúde Bucal":

        if hasattr(queryset.model, "paciente"):
            return queryset.filter(
                paciente__dentista=usuario
            )

        return queryset

    # Marketing
    if perfil.nome == "Marketing":
        return queryset.none()

    return queryset.none()


# =====================================================
# DECORATOR ANTIGO (COMPATIBILIDADE)
# =====================================================

def perfil_required(*perfis_permitidos):

    def decorator(view_func):

        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):

            if not request.user.is_authenticated:
                return redirect("login")

            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            if not hasattr(request.user, "perfil"):

                messages.error(
                    request,
                    "Usuário sem perfil cadastrado."
                )

                return redirect("dashboard")

            perfil = request.user.perfil.perfil_acesso

            if perfil is None:

                messages.error(
                    request,
                    "Usuário sem perfil de acesso."
                )

                return redirect("dashboard")

            if perfil.nome in perfis_permitidos:
                return view_func(request, *args, **kwargs)

            messages.error(
                request,
                "Você não possui permissão para acessar esta página."
            )

            return redirect("dashboard")

        return _wrapped_view

    return decorator


# =====================================================
# NOVO DECORATOR DE PERMISSÕES
# =====================================================

def permissao_required(modulo, acao="visualizar"):

    def decorator(view_func):

        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):

            if not request.user.is_authenticated:
                return redirect("login")

            if not tem_permissao(
                request.user,
                modulo,
                acao
            ):

                messages.error(
                    request,
                    "Você não possui permissão para acessar esta funcionalidade."
                )

                if (
                    request.resolver_match
                    and request.resolver_match.url_name == "dashboard"
                ):
                    return redirect("login")

                return redirect("dashboard")

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator