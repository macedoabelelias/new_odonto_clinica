# =========================================
# IMPORTAÇÕES
# =========================================

from accounts.models import Auditoria


# =========================================
# REGISTRAR AUDITORIA
# =========================================

def registrar_auditoria(
    request,
    modulo,
    acao,
    descricao,
    objeto_id=None,
    nivel="info",
    usuario=None,
):

    # =========================================
    # USUÁRIO
    # =========================================

    if usuario is None:

        if (
            request
            and hasattr(request, "user")
            and request.user.is_authenticated
        ):

            usuario = request.user

        else:

            usuario = None

    # =========================================
    # IP
    # =========================================

    ip = None

    if request:

        ip = request.META.get("REMOTE_ADDR")

    # =========================================
    # REGISTRA AUDITORIA
    # =========================================

    Auditoria.objects.create(

        usuario=usuario,

        modulo=modulo,

        acao=acao,

        descricao=descricao,

        objeto_id=objeto_id,

        nivel=nivel,

        ip=ip,

    )