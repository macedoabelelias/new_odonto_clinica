from django.core.management.base import BaseCommand

from accounts.models import Modulo


class Command(BaseCommand):
    help = "Cadastra e atualiza os módulos padrão do sistema."

    MODULOS = [

        # =====================================================
        # GERAL
        # =====================================================

        ("dashboard", "Dashboard", "Geral", "bi-speedometer2", 1),

        # =====================================================
        # ATENDIMENTO
        # =====================================================

        ("agenda", "Agenda", "Atendimento", "bi-calendar3", 10),
        ("pacientes", "Pacientes", "Atendimento", "bi-people-fill", 11),
        ("tratamentos", "Tratamentos", "Atendimento", "bi-heart-pulse-fill", 12),
        ("odontograma", "Odontograma", "Atendimento", "bi-grid-3x3-gap-fill", 13),
        ("anamnese", "Anamnese", "Atendimento", "bi-clipboard2-pulse", 14),
        ("evolucoes", "Evoluções", "Atendimento", "bi-journal-medical", 15),
        ("orcamentos", "Orçamentos", "Atendimento", "bi-clipboard2-check", 16),

        # =====================================================
        # CADASTROS
        # =====================================================

        ("procedimentos", "Procedimentos", "Cadastros", "bi-bandaid-fill", 20),
        ("convenios", "Convênios", "Cadastros", "bi-hospital", 21),

        # =====================================================
        # FINANCEIRO
        # =====================================================

        ("contas_receber", "Contas a Receber", "Financeiro", "fa-hand-holding-dollar", 30),
        ("contas_pagar", "Contas a Pagar", "Financeiro", "fa-file-invoice-dollar", 31),
        ("caixa", "Caixa", "Financeiro", "fa-cash-register", 32),

        # NOVA ETAPA 4
        ("livro_caixa", "Livro Caixa", "Financeiro", "fa-book", 33),

        # ETAPAS FUTURAS
        ("fluxo_caixa", "Fluxo de Caixa", "Financeiro", "fa-chart-line", 34),
        ("dre", "DRE Simplificada", "Financeiro", "fa-chart-pie", 35),
        ("fechamento_mensal", "Fechamento Mensal", "Financeiro", "fa-calendar-check", 36),

        # =====================================================
        # COMPRAS
        # =====================================================

        ("fornecedores", "Fornecedores", "Compras", "fa-truck-field", 40),
        ("produtos", "Produtos", "Compras", "fa-box-open", 41),
        ("compras", "Compras", "Compras", "fa-cart-shopping", 42),
        ("estoque", "Estoque", "Compras", "fa-warehouse", 43),
        ("movimentacoes_estoque", "Movimentações", "Compras", "fa-arrow-right-arrow-left", 44),
        ("produtos_criticos", "Produtos Críticos", "Compras", "fa-triangle-exclamation", 45),
        ("lotes", "Lotes", "Compras", "fa-boxes-stacked", 46),

        # =====================================================
        # RELATÓRIOS
        # =====================================================

        ("relatorios", "Central de Relatórios", "Relatórios", "bi-bar-chart-line-fill", 50),
        ("minha_producao", "Minha Produção", "Relatórios", "fa-user-doctor", 51),

        # =====================================================
        # EQUIPE
        # =====================================================

        ("usuarios", "Usuários", "Equipe", "bi-people", 60),

        # =====================================================
        # CONFIGURAÇÕES
        # =====================================================

        # =====================================================
        # CONFIGURAÇÕES
        # =====================================================

        ("perfis", "Perfis de Acesso", "Configurações", "bi-shield-lock", 70),
        ("configuracao_clinica", "Clínica", "Configurações", "bi-hospital", 71),
        ("metas_dentistas", "Metas dos Dentistas", "Configurações", "bi-bullseye", 72),
        ("meta_clinica", "Meta da Clínica", "Configurações", "bi-graph-up-arrow", 73),

        # =====================================================
        # MARKETING
        # =====================================================

        ("marketing", "Marketing", "Marketing", "fa-bullhorn", 80),

        # =====================================================
        # AUDITORIA
        # =====================================================

        ("auditoria", "Auditoria", "Auditoria", "fa-user-shield", 90),

    ]

    def handle(self, *args, **options):

        criados = 0
        atualizados = 0

        for codigo, nome, grupo, icone, ordem in self.MODULOS:

            _, criado = Modulo.objects.update_or_create(
                codigo=codigo,
                defaults={
                    "nome": nome,
                    "grupo": grupo,
                    "icone": icone,
                    "ordem": ordem,
                    "ativo": True,
                },
            )

            if criado:
                criados += 1
            else:
                atualizados += 1

        total = len(self.MODULOS)

        self.stdout.write(
            self.style.SUCCESS("=" * 60)
        )

        self.stdout.write(
            self.style.SUCCESS(f"✔ Módulos criados: {criados}")
        )

        self.stdout.write(
            self.style.SUCCESS(f"✔ Módulos atualizados: {atualizados}")
        )

        self.stdout.write(
            self.style.SUCCESS(f"✔ Total processado: {total}")
        )

        self.stdout.write(
            self.style.SUCCESS("=" * 60)
        )