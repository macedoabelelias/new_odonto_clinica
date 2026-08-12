from .models import Modulo, Permissao

# =====================================================
# MATRIZ DE PERMISSÕES PADRÃO
# =====================================================

PERMISSOES_PADRAO = {

    # =================================================
    # ADMINISTRADOR
    # =================================================

    "Administrador": {

        # =================================================
        # GERAL
        # =================================================

        "dashboard": ("v", "i", "e", "x", "p"),

        # =================================================
        # ATENDIMENTO
        # =================================================

        "agenda": ("v", "i", "e", "x", "p"),
        "pacientes": ("v", "i", "e", "x", "p"),
        "tratamentos": ("v", "i", "e", "x", "p"),
        "odontograma": ("v", "i", "e", "x", "p"),
        "anamnese": ("v", "i", "e", "x", "p"),
        "evolucoes": ("v", "i", "e", "x", "p"),
        "orcamentos": ("v", "i", "e", "x", "p"),

        # =================================================
        # FINANCEIRO
        # =================================================

        "contas_receber": ("v", "i", "e", "x", "p"),
        "contas_pagar": ("v", "i", "e", "x", "p"),
        "caixa": ("v", "i", "e", "x", "p"),
        "livro_caixa": ("v", "i", "e", "x", "p"),
        "fluxo_caixa": ("v", "i", "e", "x", "p"),
        "dre": ("v", "i", "e", "x", "p"),
        "fechamento_mensal": ("v", "i", "e", "x", "p"),

        # =================================================
        # COMPRAS
        # =================================================

        "fornecedores": ("v", "i", "e", "x", "p"),
        "produtos": ("v", "i", "e", "x", "p"),
        "compras": ("v", "i", "e", "x", "p"),
        "estoque": ("v", "i", "e", "x", "p"),
        "movimentacoes_estoque": ("v", "i", "e", "x", "p"),
        "produtos_criticos": ("v", "i", "e", "x", "p"),
        "lotes": ("v", "i", "e", "x", "p"),

        # =================================================
        # RELATÓRIOS
        # =================================================

        "relatorios": ("v", "i", "e", "x", "p"),
        "minha_producao": ("v", "i", "e", "x", "p"),

        # =================================================
        # EQUIPE
        # =================================================

        "usuarios": ("v", "i", "e", "x", "p"),

        # =================================================
        # CONFIGURAÇÕES
        # =================================================

        "perfis": ("v", "i", "e", "x", "p"),
        "configuracao_clinica": ("v", "i", "e", "x", "p"),

        # =================================================
        # MARKETING
        # =================================================

        "marketing": ("v", "i", "e", "x", "p"),

        # =================================================
        # AUDITORIA
        # =================================================

        "auditoria": ("v", "i", "e", "x", "p"),
    },


    # =====================================================
    # GESTOR
    # =====================================================

    "Gestor": {

        "dashboard": ("v",),

        # Atendimento
        "agenda": ("v", "i", "e"),
        "pacientes": ("v", "i", "e"),
        "tratamentos": ("v",),
        "orcamentos": ("v", "i", "e"),

        # Financeiro
        "contas_receber": ("v",),
        "contas_pagar": ("v",),
        "caixa": ("v",),
        "livro_caixa": ("v",),
        "fluxo_caixa": ("v",),
        "dre": ("v",),
        "fechamento_mensal": ("v",),

        # Compras
        "fornecedores": ("v", "i", "e"),
        "produtos": ("v", "i", "e"),
        "compras": ("v", "i", "e"),
        "estoque": ("v", "i", "e"),

        # Relatórios
        "relatorios": ("v", "p"),
    },


    # =====================================================
    # DENTISTA
    # =====================================================

    "Dentista": {

        "dashboard": ("v",),

        # Atendimento
        "agenda": ("v",),
        "pacientes": ("v",),
        "anamnese": ("v", "e"),
        "odontograma": ("v", "e"),
        "tratamentos": ("v", "i", "e"),
        "orcamentos": ("v", "i", "e"),
    },


    # =====================================================
    # SECRETÁRIA
    # =====================================================

    "Secretária": {

        "dashboard": ("v",),

        # Atendimento
        "agenda": ("v", "i", "e"),
        "pacientes": ("v", "i", "e"),
        "orcamentos": ("v", "i", "e"),

        # Financeiro
        "contas_receber": ("v", "i", "e"),

        # Compras
        "fornecedores": ("v",),
        "produtos": ("v",),
        "compras": ("v", "i"),
        "estoque": ("v",),

        # Relatórios
        "relatorios": ("v",),
    },


    # =====================================================
    # AUXILIAR DE SAÚDE BUCAL
    # =====================================================

    "Auxiliar de Saúde Bucal": {

        "dashboard": ("v",),

        # Atendimento
        "agenda": ("v",),
        "pacientes": ("v",),
        "tratamentos": ("v",),

        # Compras
        "estoque": ("v",),
        "produtos": ("v",),
    },


    # =====================================================
    # CONTABILIDADE
    # =====================================================

    "Contabilidade": {

        "dashboard": ("v",),

        # Financeiro
        "contas_receber": ("v", "i", "e", "p"),
        "contas_pagar": ("v", "i", "e", "p"),
        "caixa": ("v", "i", "e", "p"),
        "livro_caixa": ("v", "i", "e", "p"),
        "fluxo_caixa": ("v", "i", "e", "p"),
        "dre": ("v", "p"),
        "fechamento_mensal": ("v", "p"),

        # Relatórios
        "relatorios": ("v", "p"),
    },


    # =====================================================
    # MARKETING
    # =====================================================

    "Marketing": {

        "dashboard": ("v",),

        # Marketing
        "marketing": ("v", "i", "e"),

        # Relatórios
        "relatorios": ("v", "p"),
    },


    # =====================================================
    # AUDITORIA
    # =====================================================

    "Auditoria": {

        # =================================================
        # DASHBOARD
        # =================================================

        # IMPORTANTE:
        # O perfil precisa visualizar o Dashboard
        # para conseguir entrar normalmente no sistema.

        "dashboard": ("v",),

        # =================================================
        # ÁREA DE AUDITORIA
        # =================================================

        "auditoria": ("v", "i", "e", "x", "p"),
    },
}
               

    
# =====================================================
# APLICAR PERMISSÕES PADRÃO
# =====================================================

def aplicar_permissoes_padrao(perfil):

    permissoes = PERMISSOES_PADRAO.get(perfil.nome)

    if not permissoes:
        return

    for codigo_modulo, acoes in permissoes.items():

        try:
            modulo = Modulo.objects.get(
                codigo=codigo_modulo,
                ativo=True
            )

        except Modulo.DoesNotExist:

            print(f'⚠️ Módulo "{codigo_modulo}" não encontrado.')
            continue

        permissao, criado = Permissao.objects.get_or_create(
            perfil=perfil,
            modulo=modulo
        )

        permissao.visualizar = "v" in acoes
        permissao.inserir = "i" in acoes
        permissao.editar = "e" in acoes
        permissao.excluir = "x" in acoes
        permissao.exportar = "p" in acoes

        permissao.save()