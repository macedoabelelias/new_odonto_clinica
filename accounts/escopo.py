# accounts/escopo.py

from .models import PerfilUsuario


def usuario_eh_admin(user):
    if not user.is_authenticated:
        return False

    return (
        hasattr(user, "perfil")
        and user.perfil.tipo_usuario in (
            PerfilUsuario.ADMIN,
            PerfilUsuario.GESTOR,
        )
    )


def usuario_eh_dentista(user):
    if not user.is_authenticated:
        return False

    return (
        hasattr(user, "perfil")
        and user.perfil.tipo_usuario == PerfilUsuario.DENTISTA
    )
    
