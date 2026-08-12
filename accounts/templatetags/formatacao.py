from decimal import Decimal

from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()


@register.filter(name="moeda")
def moeda(valor):
    """
    Formata valores monetários para o padrão brasileiro.

    Exemplo:
    7072.35 -> R$ 7.072,35
    """

    if valor is None:
        return "R$ 0,00"

    try:
        valor = Decimal(valor)

        texto = f"{valor:.2f}"

        inteiro, decimal = texto.split(".")

        inteiro = intcomma(inteiro).replace(",", ".")

        return f"R$ {inteiro},{decimal}"

    except Exception:
        return "R$ 0,00"