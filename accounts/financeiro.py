from decimal import Decimal

from django.contrib.auth.models import User

from .models import (
    LivroCaixa,
    PerfilUsuario,
)


def registrar_livro_caixa(
    *,
    data,
    tipo,
    origem,
    descricao,
    valor,
    paciente=None,
    fornecedor=None,
    profissional=None,
    conta_receber=None,
    conta_pagar=None,
    observacao=""
):
    # =========================================
    # GARANTE DECIMAL
    # =========================================

    valor = Decimal(str(valor))

    # =========================================
    # CONVERTE USER -> PERFILUSUARIO
    # =========================================

    if isinstance(profissional, User):

        try:

            profissional = PerfilUsuario.objects.get(
                usuario=profissional
            )

        except PerfilUsuario.DoesNotExist:

            profissional = None

    # =========================================
    # OBTÉM O ÚLTIMO SALDO
    # =========================================

    ultimo = LivroCaixa.objects.order_by(
        "-data",
        "-id"
    ).first()

    saldo_anterior = (
        ultimo.saldo
        if ultimo
        else Decimal("0.00")
    )

    # =========================================
    # CALCULA ENTRADA / SAÍDA
    # =========================================

    if tipo == "ENTRADA":

        entrada = valor
        saida = Decimal("0.00")
        saldo = saldo_anterior + valor

    else:

        entrada = Decimal("0.00")
        saida = valor
        saldo = saldo_anterior - valor

    # =========================================
    # REGISTRA O LANÇAMENTO
    # =========================================

    return LivroCaixa.objects.create(

        data=data,

        tipo=tipo,

        origem=origem,

        descricao=descricao,

        entrada=entrada,

        saida=saida,

        saldo=saldo,

        paciente=paciente,

        fornecedor=fornecedor,

        profissional=profissional,

        conta_receber=conta_receber,

        conta_pagar=conta_pagar,

        observacao=observacao

    )