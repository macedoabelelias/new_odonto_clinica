from .permissions import tem_permissao


def permissoes_sidebar(request):
    """
    Disponibiliza as permissões do usuário para todos os templates.
    """

    if not request.user.is_authenticated:

        return {
            "perms_sidebar": {}
        }

    def pode(modulo):
        try:
            return tem_permissao(
                request.user,
                modulo
            )
        except Exception:
            return False

    return {

        "perms_sidebar": {

            "agenda": pode("agenda"),

            "pacientes": pode("pacientes"),

            "procedimentos": pode("procedimentos"),

            "convenios": pode("convenios"),

            "orcamentos": pode("orcamentos"),

            "relatorios": pode("relatorios"),

            "financeiro": pode("financeiro"),

            "compras": pode("compras"),

            "configuracoes": pode("configuracoes"),

        }

    }