from .models import Permissao


def usuario_tem_permissao(user, modulo_codigo, acao="visualizar"):
    """
    Verifica se o usuário possui permissão para um módulo.
    """

    if not user.is_authenticated:
        return False

    if user.is_superuser:
        return True

    if not hasattr(user, "perfil"):
        return False

    perfil_usuario = user.perfil

    if not perfil_usuario.ativo:
        return False

    if perfil_usuario.perfil_acesso is None:
        return False

    try:

        permissao = Permissao.objects.get(
            perfil=perfil_usuario.perfil_acesso,
            modulo__codigo=modulo_codigo
        )

    except Permissao.DoesNotExist:
        return False

    return getattr(permissao, acao, False)