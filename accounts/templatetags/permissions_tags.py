from django import template

register = template.Library()

@register.simple_tag
def possui_permissao(user, modulo, acao="visualizar"):

    print(
        "TAG:",
        user.username,
        modulo,
        acao
    )

    from accounts.permissions import tem_permissao

    resultado = tem_permissao(user, modulo, acao)

    print("RESULTADO:", resultado)

    return resultado