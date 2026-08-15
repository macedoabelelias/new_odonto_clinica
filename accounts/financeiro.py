from decimal import Decimal

from django.contrib.auth.models import User

from .models import (
    LivroCaixa,
    PerfilUsuario,
    FechamentoMensal,
)


# =========================================
# REGISTRAR LIVRO CAIXA
# =========================================

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
    # EVITA DUPLICIDADE
    # =========================================
    #
    # Uma Conta a Receber só pode gerar
    # um lançamento no Livro Caixa.
    #
    # Uma Conta a Pagar também só pode gerar
    # um lançamento no Livro Caixa.
    #
    # =========================================

    if conta_receber is not None:

        existente = LivroCaixa.objects.filter(
            conta_receber=conta_receber
        ).first()

        if existente:
            return existente

    if conta_pagar is not None:

        existente = LivroCaixa.objects.filter(
            conta_pagar=conta_pagar
        ).first()

        if existente:
            return existente

    # =========================================
    # OBTÉM O ÚLTIMO SALDO
    # =========================================

    ultimo = (
        LivroCaixa.objects
        .order_by("-data", "-id")
        .first()
    )

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

        saldo = (
            saldo_anterior + valor
        )

    else:

        entrada = Decimal("0.00")
        saida = valor

        saldo = (
            saldo_anterior - valor
        )

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

        observacao=observacao,

    )


# =========================================
# VERIFICA COMPETÊNCIA FECHADA
# =========================================

def competencia_fechada(data):
    """
    Retorna True quando a competência correspondente
    à data informada estiver fechada.
    """

    if not data:
        return False

    return FechamentoMensal.objects.filter(

        ano=data.year,

        mes=data.month,

        status="FECHADO"

    ).exists()