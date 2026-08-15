from django.urls import path

from . import views


urlpatterns = [

    # =========================================
    # LOGIN
    # =========================================

    path(
        '',
        views.login_view,
        name='login'
    ),

    # =========================================
    # DASHBOARD
    # =========================================

    path(
        'dashboard/',
        views.dashboard_view,
        name='dashboard'
    ),

    # =========================================
    # DASHBOARD DE AUDITORIA
    # =========================================

    path(
        'auditoria/dashboard/',
        views.dashboard_auditoria,
        name='auditoria'
    ),

    path(
        'auditoria/dashboard/',
        views.dashboard_auditoria,
        name='dashboard_auditoria'
    ),

    # =========================================
    # PACIENTES
    # =========================================

    path(
        'pacientes/',
        views.pacientes_view,
        name='pacientes'
    ),

    # =========================================
    # PERFIL DO PACIENTE
    # =========================================

    path(
        'pacientes/novo/',
        views.novo_paciente,
        name='novo_paciente'
    ),

    path(
        'pacientes/<int:id>/',
        views.perfil_paciente,
        name='perfil_paciente'
    ),
    

    # =========================================
    # EDITAR PACIENTE
    # =========================================

    path(
        'pacientes/editar/<int:id>/',
        views.editar_paciente,
        name='editar_paciente'
    ),

    path(
        'pacientes/excluir/<int:id>/',
        views.excluir_paciente,
        name='excluir_paciente'
    ),

    path(
        'pacientes/<int:id>/status/',
        views.alterar_status_paciente,
        name='alterar_status_paciente'
    ),

    # =========================================
    # ODONTOGRAMA
    # =========================================

    path(
        'pacientes/<int:id>/odontograma/',
        views.odontograma,
        name='odontograma'
    ),

    # =========================================
    # POSICIONAMENTO DOS DENTES
    # =========================================

    path(
        "pacientes/<int:id>/odontograma/posicionamento/",
        views.salvar_posicionamento_dente,
        name="salvar_posicionamento_dente",
    ),

# =========================================
# MARKETING - LEADS
# =========================================

path(
    "marketing/leads/",
    views.leads,
    name="leads",
),

# =========================================
# LEADS - NOVO
# =========================================

path(
    "marketing/leads/novo/",
    views.novo_lead,
    name="novo_lead",
),

# =========================================
# DASHBOARD MARKETING
# =========================================

path(
    "marketing/dashboard/",
    views.dashboard_marketing,
    name="dashboard_marketing",
),

# =========================================
# LEAD - DETALHE
# =========================================

path(
    "marketing/leads/<int:pk>/",
    views.detalhe_lead,
    name="detalhe_lead",
),

# =========================================
# LEAD - EDITAR
# =========================================

path(
    "marketing/leads/<int:pk>/editar/",
    views.editar_lead,
    name="editar_lead",
),

# =========================================
# LEAD - EXCLUIR
# =========================================

path(
    "marketing/leads/<int:pk>/excluir/",
    views.excluir_lead,
    name="excluir_lead",
),


# =========================================
# CAMPANHAS DE MARKETING
# =========================================

path(
    "marketing/campanhas/",
    views.campanhas_marketing,
    name="campanhas_marketing",
),

# =========================================
# NOVA CAMPANHA
# =========================================

path(
    "marketing/campanhas/nova/",
    views.nova_campanha_marketing,
    name="campanhas_marketing_nova",
),

# =========================================
# PÁGINA PÚBLICA DA CAMPANHA
# =========================================

path(
    "marketing/campanha/<int:pk>/",
    views.campanha_publica,
    name="campanha_publica",
),

# =========================================
# DETALHE DA CAMPANHA
# =========================================

path(
    "marketing/campanhas/<int:pk>/",
    views.detalhe_campanha_marketing,
    name="detalhe_campanha_marketing",
),

# =========================================
# EDITAR CAMPANHA
# =========================================

path(
    "marketing/campanhas/<int:pk>/editar/",
    views.editar_campanha_marketing,
    name="editar_campanha_marketing",
),

# =========================================
# EXCLUIR CAMPANHA
# =========================================

path(
    "marketing/campanhas/<int:pk>/excluir/",
    views.excluir_campanha_marketing,
    name="excluir_campanha_marketing",
),

# =========================================
# CAPTAÇÃO PÚBLICA DE CAMPANHA
# =========================================

path(
    "campanha/<int:pk>/",
    views.captacao_campanha,
    name="captacao_campanha",
),

# =========================================
# CAMPANHA PÚBLICA
# =========================================

path(
    "campanha/<int:pk>/",
    views.campanha_publica,
    name="campanha_publica",
),

# =========================================
# ODONTOGRAMA
# =========================================

path(
    'pacientes/<int:id>/odontograma/',
    views.odontograma,
    name='odontograma'
),

# =========================================
# TRATAMENTOS
# =========================================

path(
    'pacientes/<int:id>/tratamentos/',
    views.tratamentos_paciente,
    name='tratamentos_paciente'
),

# =========================================
# PROCEDIMENTO GERAL
# =========================================

path(
    'pacientes/<int:id>/procedimento-geral/',
    views.salvar_procedimento_geral,
    name='salvar_procedimento_geral'
),

    # =========================================
    # ANAMNESE
    # =========================================

    path(
        'pacientes/<int:id>/anamnese/',
        views.anamnese,
        name='anamnese'
    ),

    # =========================================
    # FICHA CLÍNICA
    # =========================================

    path(
        'pacientes/<int:id>/ficha-clinica/',
        views.ficha_clinica,
        name='ficha_clinica'
    ),
    
    path(
        'pacientes/<int:id>/anexo/',
        views.upload_anexo,
        name='upload_anexo'
    ),

    # =========================================
    # ORÇAMENTO
    # =========================================

    path(
        'pacientes/<int:id>/orcamento/',
        views.orcamento,
        name='orcamento'
    ),

    path(
        'orcamento/<int:id>/pdf/',
        views.gerar_pdf_orcamento,
        name='gerar_pdf_orcamento'
    ),

    path(
        'documento/novo/<int:id>/',
        views.novo_documento,
        name='novo_documento'
    ),

    path(
        'documento/editar/<int:id>/',
        views.editar_documento,
        name='editar_documento'
    ),

    path(
        'documento/visualizar/<int:id>/',
        views.visualizar_documento,
        name='visualizar_documento'
    ),
       
    # =========================================
    # PROCEDIMENTOS
    # =========================================

    path(
        'procedimentos/',
        views.procedimentos,
        name='procedimentos'
    ),

   path(
        'pacientes/<int:id>/procedimento-geral/',
        views.salvar_procedimento_geral,
        name='procedimento_geral'
    ),

    # =========================================
    # LOGOUT
    # =========================================

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    path(
        'convenios/',
        views.convenios,
        name='convenios'
    ),

path(
    'procedimentos/editar/<int:id>/',
    views.editar_procedimento,
    name='editar_procedimento'
),

path(
    'procedimentos/excluir/<int:id>/',
    views.excluir_procedimento,
    name='excluir_procedimento'
),


path(
    'convenios/editar/<int:id>/',
    views.editar_convenio,
    name='editar_convenio'
),

path(
    'convenios/excluir/<int:id>/',
    views.excluir_convenio,
    name='excluir_convenio'
),

path(

    'orcamento/item/<int:id>/excluir/',

    views.excluir_item_orcamento,

    name='excluir_item_orcamento'

),

path(

    'orcamento/item/<int:id>/editar/',

    views.editar_item_orcamento,

    name='editar_item_orcamento'

),

path(
    'procedimento/<int:id>/status/',
    views.alterar_status_procedimento,
    name='alterar_status_procedimento'
),

path(

    'pacientes/<int:id>/prontuario/pdf/',

    views.imprimir_prontuario,

    name='imprimir_prontuario'

),

path(
    'pacientes/<int:id>/anamnese/pdf/',
    views.imprimir_anamnese,
    name='imprimir_anamnese'
),

path(
    'configuracao-clinica/',
    views.configuracao_clinica,
    name='configuracao_clinica'
),

path(
    'documento/<int:id>/pdf/',
    views.imprimir_documento,
    name='imprimir_documento'
),

# =========================================
# USUÁRIOS
# =========================================

path(
    'usuarios/',
    views.usuarios,
    name='usuarios'
),

path(
    'usuarios/novo/',
    views.novo_usuario,
    name='novo_usuario'
),

path(
    'usuarios/<int:id>/editar/',
    views.editar_usuario,
    name='editar_usuario'
),

path(
    'usuarios/<int:id>/ativar/',
    views.ativar_usuario,
    name='ativar_usuario'
),

path(
    'usuarios/<int:id>/desativar/',
    views.desativar_usuario,
    name='desativar_usuario'
),

# =========================================
# MEDICAMENTOS
# =========================================

path(
    'medicamentos/',
    views.medicamentos,
    name='medicamentos'
),

path(
    'medicamentos/novo/',
    views.novo_medicamento,
    name='novo_medicamento'
),

# =========================================
# RECEITAS
# =========================================

path(
    'pacientes/<int:id>/receitas/',
    views.receitas,
    name='receitas'
),

path(
    'pacientes/<int:id>/receita/nova/',
    views.nova_receita,
    name='nova_receita'
),

path(
    'receita/editar/<int:id>/',
    views.editar_receita,
    name='editar_receita'
),

path(
    'receita/excluir/<int:id>/',
    views.excluir_receita,
    name='excluir_receita'
),

path(
    'receita/<int:id>/pdf/',
    views.imprimir_receita,
    name='imprimir_receita'
),

path(
    'modelo-receita/<int:id>/',
    views.buscar_modelo_receita,
    name='buscar_modelo_receita'
),

path(
    'modelos-receita/',
    views.modelos_receita,
    name='modelos_receita'
),

path(
    'modelos-receita/<int:id>/editar/',
    views.editar_modelo_receita,
    name='editar_modelo_receita'
),

path(
    'modelos-receita/<int:id>/excluir/',
    views.excluir_modelo_receita,
    name='excluir_modelo_receita'
),

# =========================================
# EXAMES
# =========================================

path(
    'pacientes/<int:id>/exames/',
    views.exames,
    name='exames'
),

path(
    'pacientes/<int:id>/exame/novo/',
    views.novo_exame,
    name='novo_exame'
),

path(
    'exame/<int:id>/excluir/',
    views.excluir_exame,
    name='excluir_exame'
),

path(
    'pacientes/<int:id>/procedimento-geral/',
    views.salvar_procedimento_geral,
    name='salvar_procedimento_geral'
),

path(
    'documento/excluir/<int:id>/',
    views.excluir_documento,
    name='excluir_documento'
),

# =========================================
# SOLICITAÇÕES DE EXAMES
# =========================================

path(
    'pacientes/<int:id>/solicitacoes-exames/',
    views.solicitacoes_exames,
    name='solicitacoes_exames'
),

path(
    'pacientes/<int:id>/solicitacao-exame/nova/',
    views.nova_solicitacao_exame,
    name='nova_solicitacao_exame'
),

path(
    'solicitacao-exame/<int:id>/excluir/',
    views.excluir_solicitacao_exame,
    name='excluir_solicitacao_exame'
),

path(
    'solicitacao-exame/<int:id>/pdf/',
    views.imprimir_solicitacao_exame,
    name='imprimir_solicitacao_exame'
),

path(
    'fornecedores/',
    views.fornecedores,
    name='fornecedores'
),

path(
    'fornecedores/novo/',
    views.novo_fornecedor,
    name='novo_fornecedor'
),

path(
    'meu-perfil/',
    views.meu_perfil,
    name='meu_perfil'
),

path(
    'alterar-senha/',
    views.alterar_senha,
    name='alterar_senha'
),

path(
    'usuarios/<int:id>/status/',
    views.alterar_status_usuario,
    name='alterar_status_usuario'
),

path(
    'fornecedores/novo/',
    views.novo_fornecedor,
    name='novo_fornecedor'
),

path(
    'fornecedores/<int:fornecedor_id>/editar/',
    views.editar_fornecedor,
    name='editar_fornecedor'
),

path(
    'fornecedores/<int:fornecedor_id>/status/',
    views.alterar_status_fornecedor,
    name='alterar_status_fornecedor'
),

path(
    'fornecedores/<int:fornecedor_id>/excluir/',
    views.excluir_fornecedor,
    name='excluir_fornecedor'
),

# =========================================
# PRODUTOS
# =========================================

path(
    'produtos/',
    views.produtos,
    name='produtos'
),

path(
    'estoque/',
    views.estoque,
    name='estoque'
),

path(
    'estoque/movimentacoes/',
    views.movimentacoes_estoque,
    name='movimentacoes_estoque'
),

path(
    'estoque/movimentacoes/nova/',
    views.nova_movimentacao_estoque,
    name='nova_movimentacao_estoque'
),

path(
    'produtos/novo/',
    views.novo_produto,
    name='novo_produto'
),

path(
    'produtos/<int:produto_id>/editar/',
    views.editar_produto,
    name='editar_produto'
),

path(
    'produtos/<int:produto_id>/status/',
    views.alterar_status_produto,
    name='alterar_status_produto'
),

path(
    'produtos/<int:produto_id>/excluir/',
    views.excluir_produto,
    name='excluir_produto'
),

path(
    'estoque/produtos-criticos/',
    views.produtos_criticos,
    name='produtos_criticos'
),

path(
    'lotes/',
    views.lotes,
    name='lotes'
),

path(
    'lotes/novo/',
    views.novo_lote,
    name='novo_lote'
),

# =========================================
# COMPRAS
# =========================================

path(
    'compras/',
    views.compras,
    name='compras'
),

path(
    'compras/nova/',
    views.nova_compra,
    name='nova_compra'
),

path(
    'compras/<int:compra_id>/',
    views.visualizar_compra,
    name='visualizar_compra'
),

path(
    'compras/<int:compra_id>/editar/',
    views.editar_compra,
    name='editar_compra'
),

path(
    'compras/<int:compra_id>/excluir/',
    views.excluir_compra,
    name='excluir_compra'
),

# =========================================
# CONTAS A PAGAR
# =========================================

path(
    'financeiro/contas-pagar/',
    views.contas_pagar,
    name='contas_pagar'
),

path(
    'financeiro/contas-pagar/nova/',
    views.nova_conta_pagar,
    name='nova_conta_pagar'
),

path(
    'financeiro/contas-pagar/<int:conta_id>/pagar/',
    views.pagar_conta,
    name='pagar_conta'
),

# =========================================
# CONTAS A RECEBER
# =========================================

path(
    'financeiro/contas-receber/',
    views.contas_receber,
    name='contas_receber'
),

path(
    'orcamento/<int:id>/aprovar/',
    views.aprovar_orcamento,
    name='aprovar_orcamento'
),

path(
    'financeiro/contas-receber/<int:conta_id>/receber/',
    views.receber_conta,
    name='receber_conta'
),

path(
    'financeiro/caixa/',
    views.caixa,
    name='caixa'
),

path(
    'financeiro/caixa/abrir/',
    views.abrir_caixa,
    name='abrir_caixa'
),

path(
    'financeiro/caixa/fechar/',
    views.fechar_caixa,
    name='fechar_caixa'
),

path(
    "financeiro/caixa/reabrir/",
    views.reabrir_caixa,
    name="reabrir_caixa",
),

# =========================================
# LIVRO CAIXA
# =========================================

path(
    "financeiro/livro-caixa/",
    views.livro_caixa,
    name="livro_caixa",
),

path(
    "financeiro/dre/",
    views.dre,
    name="dre"
),

# =========================================
# FECHAMENTO MENSAL
# =========================================

path(
    "financeiro/fechamento-mensal/",
    views.fechamento_mensal,
    name="fechamento_mensal",
),

path(
    'orcamentos/central/',
    views.central_orcamentos,
    name='central_orcamentos'
),

path(
    'orcamentos/<int:id>/excluir/',
    views.excluir_orcamento,
    name='excluir_orcamento'
),

# =========================================
# ENCERRAR TRATAMENTOS
# =========================================

path(
    "tratamentos/<int:tratamento_id>/encerrar/",
    views.encerrar_tratamento,
    name="encerrar_tratamento",
),

# =========================================
# NOVO TRATAMENTO
# =========================================

path(
    "pacientes/<int:paciente_id>/novo-tratamento/",
    views.novo_tratamento,
    name="novo_tratamento",
),

path(
    "tratamentos/<int:tratamento_id>/cancelar/",
    views.cancelar_tratamento,
    name="cancelar_tratamento",
),

path(
    'relatorios/',
    views.central_relatorios,
    name='central_relatorios'
),

path(
    'relatorios/pacientes/',
    views.relatorio_pacientes,
    name='relatorio_pacientes'
),

path(
    'relatorios/tratamentos/',
    views.relatorio_tratamentos,
    name='relatorio_tratamentos'
),

path(
    'relatorios/orcamentos/',
    views.relatorio_orcamentos,
    name='relatorio_orcamentos'
),

path(
    'relatorios/agenda/',
    views.relatorio_agenda,
    name='relatorio_agenda'
),

path(
    'relatorios/receber/',
    views.relatorio_receber,
    name='relatorio_receber'
),

path(
    'relatorios/pagar/',
    views.relatorio_pagar,
    name='relatorio_pagar'
),

path(
    'relatorios/caixa/',
    views.relatorio_caixa,
    name='relatorio_caixa'
),

path(
    'relatorios/indicadores/',
    views.relatorio_indicadores,
    name='relatorio_indicadores'
),

path(
    'relatorios/producao/',
    views.relatorio_producao,
    name='relatorio_producao'
),

path(
    'relatorios/faturamento/',
    views.relatorio_faturamento,
    name='relatorio_faturamento'
),

# =========================================
# PDF RELATÓRIO DE PACIENTES
# =========================================

path(

    'relatorios/pacientes/pdf/',
    views.gerar_pdf_relatorio_pacientes,
    name='pdf_relatorio_pacientes'

),

path(
    'relatorios/tratamentos/pdf/',
    views.pdf_relatorio_tratamentos,
    name='pdf_relatorio_tratamentos'
),

path(
    'relatorios/orcamentos/',
    views.relatorio_orcamentos,
    name='relatorio_orcamentos'
),

path(
    "relatorios/orcamentos/pdf/",
    views.relatorio_orcamentos_pdf,
    name="relatorio_orcamentos_pdf",
),

path(
    "relatorios/atendimentos/",
    views.relatorio_atendimentos,
    name="relatorio_atendimentos",
),

path(
    "relatorios/atendimentos/pdf/",
    views.relatorio_atendimentos_pdf,
    name="relatorio_atendimentos_pdf",
),

path(
    "relatorios/contas-receber/",
    views.relatorio_contas_receber,
    name="relatorio_contas_receber",
),

path(
    "relatorios/contas-receber/pdf/",
    views.relatorio_contas_receber_pdf,
    name="relatorio_contas_receber_pdf",
),

path(
    "relatorios/contas-pagar/",
    views.relatorio_contas_pagar,
    name="relatorio_contas_pagar",
),

path(
    "relatorios/contas-pagar/pdf/",
    views.relatorio_contas_pagar_pdf,
    name="relatorio_contas_pagar_pdf",
),

path(
    "relatorios/caixa/",
    views.relatorio_caixa,
    name="relatorio_caixa",
),

path(
    "relatorios/caixa/pdf/",
    views.relatorio_caixa_pdf,
    name="relatorio_caixa_pdf",
),

# =========================================
# CENTRAL DE PRODUÇÃO
# =========================================

path(
    "relatorios/producao/",
    views.relatorio_producao,
    name="relatorio_producao"
),

# =========================================
# PRODUÇÃO POR PROFISSIONAL
# =========================================

path(
    "relatorios/producao-profissional/",
    views.relatorio_producao_profissional,
    name="relatorio_producao_profissional"
),

path(
    "relatorios/producao-profissional/pdf/",
    views.pdf_producao_profissional,
    name="pdf_producao_profissional",
),

# =========================================
# PRODUÇÃO POR PROCEDIMENTO
# =========================================

path(
    "relatorios/producao-procedimento/",
    views.relatorio_producao_procedimento,
    name="relatorio_producao_procedimento"
),

path(
    "relatorios/producao-procedimento/pdf/",
    views.pdf_producao_procedimento,
    name="pdf_producao_procedimento",
),

# =========================================
# PRODUÇÃO MENSAL
# =========================================

path(
    "relatorios/producao-mensal/",
    views.relatorio_producao_mensal,
    name="relatorio_producao_mensal",
),

path(
    "relatorios/producao-mensal/pdf/",
    views.pdf_producao_mensal,
    name="pdf_producao_mensal",
),

# =========================================
# PRODUÇÃO CONVÊNIO
# =========================================
path(
    "relatorios/producao-convenio/",
    views.relatorio_producao_convenio,
    name="relatorio_producao_convenio",
),

path(
    "relatorios/producao-convenio/pdf/",
    views.pdf_producao_convenio,
    name="pdf_producao_convenio",
),

# =========================================
# FATURAMENTO
# =========================================

path(
    "relatorios/faturamento/",
    views.relatorio_faturamento,
    name="relatorio_faturamento",
),

path(
    "relatorios/faturamento/pdf/",
    views.pdf_faturamento,
    name="pdf_faturamento",
),

path(
    "relatorios/auditoria/",
    views.relatorio_auditoria,
    name="relatorio_auditoria",
),

# =========================================
# AUDITORIA
# =========================================

path(
    "relatorios/auditoria/pdf/",
    views.pdf_auditoria,
    name="pdf_auditoria",
),

# =========================================
# EXCEL - AUDITORIA
# =========================================

path(
    "relatorios/auditoria/excel/",
    views.excel_auditoria,
    name="excel_auditoria",
),

path(
    "relatorios/pacientes/excel/",
    views.exportar_excel_relatorio_pacientes,
    name="exportar_excel_relatorio_pacientes",
),

path(
    "relatorios/producao-mensal/excel/",
    views.excel_producao_mensal,
    name="excel_producao_mensal",
),

path(
    "relatorios/producao-procedimento/excel/",
    views.excel_producao_procedimento,
    name="excel_producao_procedimento",
),

path(
    "relatorios/faturamento/excel/",
    views.excel_faturamento,
    name="excel_faturamento",
),

path(
    "relatorios/tratamentos/excel/",
    views.excel_tratamentos,
    name="excel_tratamentos",
),

# =========================================
# EXCEL - RELATÓRIO DE ORÇAMENTOS
# =========================================
path(
    "relatorios/orcamentos/excel/",
    views.excel_orcamentos,
    name="excel_orcamentos",
),

# =========================================
# EXCEL - RELATÓRIO DE ATENDIMENTOS
# =========================================

path(
    "relatorios/atendimentos/excel/",
    views.excel_atendimentos,
    name="excel_atendimentos",
),

# =========================================
# EXCEL - PRODUÇÃO POR PROFISSIONAL
# =========================================

path(
    "relatorios/producao-profissional/excel/",
    views.excel_producao_profissional,
    name="excel_producao_profissional",
),

# =========================================
# EXCEL - PRODUÇÃO POR CONVÊNIO
# =========================================

path(
    "relatorios/producao-convenio/excel/",
    views.excel_producao_convenio,
    name="excel_producao_convenio",
),

# =========================================
# EXCEL - AUDITORIA
# =========================================

path(
    "relatorios/auditoria/excel/",
    views.excel_auditoria,
    name="excel_auditoria",
),

# =========================================
# PERFIL DO USUÁRIO
# =========================================

path(
    "perfis/",
    views.perfis,
    name="perfis"
),


path(
    "usuarios/<int:id>/",
    views.perfil_usuario,
    name="perfil_usuario"
),

path(
    "usuarios/<int:id>/editar/",
    views.editar_usuario,
    name="editar_usuario",
),

path(
    "perfis/novo/",
    views.novo_perfil,
    name="novo_perfil"
),


path(
    "perfis/<int:perfil_id>/",
    views.perfil_detalhes,
    name="perfil_detalhes",
),

path(
    "criar-perfis/",
    views.criar_perfis,
    name="criar_perfis",
),

path(
    "perfis/<int:perfil_id>/editar/",
    views.editar_perfil,
    name="editar_perfil",
),

path(
    "criar-modulos/",
    views.criar_modulos,
    name="criar_modulos",
),

path(
    "perfis/<int:perfil_id>/permissoes/",
    views.permissoes_perfil,
    name="permissoes_perfil",
),

path(
    "perfis/<int:perfil_id>/aplicar-permissoes/",
    views.aplicar_permissoes_padrao_view,
    name="aplicar_permissoes_padrao",
),

# =========================================
# FUNCIONÁRIOS DO PERFIL
# =========================================

path(
    "perfis/<int:perfil_id>/funcionarios/",
    views.funcionarios_perfil,
    name="funcionarios_perfil",
),

path(
    'relatorios/aniversariantes/',
    views.relatorio_aniversariantes,
    name='relatorio_aniversariantes'
),

# =========================================
# PDF RELATÓRIO DE ANIVERSARIANTES
# =========================================

path(
    'relatorios/aniversariantes/pdf/',
    views.gerar_pdf_relatorio_aniversariantes,
    name='pdf_relatorio_aniversariantes'
),

path(
    "metas-dentistas/",
    views.metas_dentistas,
    name="metas_dentistas",
),

path(
    "metas-dentistas/<int:pk>/editar/",
    views.editar_meta_dentista,
    name="editar_meta_dentista",
),



]


