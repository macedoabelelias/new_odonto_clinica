from django.db import models
from decimal import Decimal, ROUND_HALF_UP

from datetime import date

from django.contrib.auth.models import User
from django.conf import settings

from django.utils import timezone

import re
from urllib.parse import quote

# =========================================
# PACIENTES
# =========================================

class Paciente(models.Model):

    # =========================================
    # DADOS PESSOAIS
    # =========================================

    foto = models.ImageField(
        upload_to='pacientes/',
        blank=True,
        null=True
    )

    nome = models.CharField(
        max_length=200
    )

    cpf = models.CharField(
        max_length=14,
        blank=True,
        null=True
    )

    rg = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    nascimento = models.DateField(
        blank=True,
        null=True
    )

    genero = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    estado_civil = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    profissao = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

        # =========================================
    # CONTATO
    # =========================================

    telefone = models.CharField(
        "Telefone",
        max_length=20,
        blank=True,
        null=True,
    )

    whatsapp = models.CharField(
        "WhatsApp",
        max_length=20,
        blank=True,
        null=True,
    )

    email = models.EmailField(
        "E-mail",
        blank=True,
        null=True,
    )

    # =========================================
    # ENDEREÇO
    # =========================================

    cep = models.CharField(
        "CEP",
        max_length=10,
        blank=True,
        null=True,
    )

    endereco = models.CharField(
        "Endereço",
        max_length=255,
        blank=True,
        null=True,
    )

    numero = models.CharField(
        "Número",
        max_length=20,
        blank=True,
        null=True,
    )

    complemento = models.CharField(
        "Complemento",
        max_length=100,
        blank=True,
        null=True,
    )

    bairro = models.CharField(
        "Bairro",
        max_length=100,
        blank=True,
        null=True,
    )

    cidade = models.CharField(
        "Cidade",
        max_length=100,
        blank=True,
        null=True,
        db_index=True,
    )

    estado = models.CharField(
        "UF",
        max_length=2,
        blank=True,
        null=True,
    )

    # =========================================
    # DADOS CLÍNICOS
    # =========================================

    convenio = models.CharField(
        "Convênio",
        max_length=100,
        blank=True,
        null=True,
    )

    carteirinha = models.CharField(
        "Carteirinha",
        max_length=100,
        blank=True,
        null=True,
    )

    alergias = models.TextField(
        "Alergias",
        blank=True,
        null=True,
    )

    medicamentos = models.TextField(
        "Medicamentos em uso",
        blank=True,
        null=True,
    )

    observacoes = models.TextField(
        "Observações",
        blank=True,
        null=True,
    )

    # =========================================
    # RESPONSÁVEL
    # =========================================

    responsavel = models.CharField(
        "Responsável",
        max_length=200,
        blank=True,
        null=True,
    )

    cpf_responsavel = models.CharField(
        "CPF do Responsável",
        max_length=14,
        blank=True,
        null=True,
    )

    telefone_responsavel = models.CharField(
        "Telefone do Responsável",
        max_length=20,
        blank=True,
        null=True,
    )

    # =========================================
    # DENTISTA RESPONSÁVEL
    # =========================================

    dentista = models.ForeignKey(
        User,
        verbose_name="Dentista Responsável",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pacientes_responsavel",
    )

    # =========================================
    # CONTROLE
    # =========================================

    ativo = models.BooleanField(
        default=True,
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
    )

    atualizado_em = models.DateTimeField(
        auto_now=True,
    )

    # =========================================
    # IDADE AUTOMÁTICA
    # =========================================

    @property
    def idade(self):

        if self.nascimento:

            hoje = date.today()

            return (

                hoje.year
                - self.nascimento.year
                - (
                    (
                        hoje.month,
                        hoje.day
                    ) < (
                        self.nascimento.month,
                        self.nascimento.day
                    )
                )

            )

        return None
    
    # =========================================
    # STATUS
    # =========================================

    @property
    def status(self):

        return "Ativo" if self.ativo else "Inativo"

    # =========================================
    # TRATAMENTO ATIVO
    # =========================================

    @property
    def tratamento_ativo(self):

        return self.tratamentos.filter(
            status="ATIVO"
        ).first()

        # =========================================
    # WHATSAPP
    # =========================================

    @property
    def whatsapp_limpo(self):

        numero = self.whatsapp or self.telefone or ""

        return re.sub(r"\D", "", numero)

    @property
    def whatsapp_url(self):

        numero = self.whatsapp_limpo

        if not numero:

            return ""

        mensagem = (
            f"Olá, {self.nome}! 😊\n\n"
            f"Estamos confirmando sua consulta na "
            f"AM Systems Odontologia."
        )

        return (
            f"https://wa.me/55{numero}"
            f"?text={quote(mensagem)}"
        )

    # =========================================
    # STRING
    # =========================================
    
    def __str__(self):

        return self.nome 

class Anamnese(models.Model):

    paciente = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE
    )

    # =========================================
    # QUEIXA PRINCIPAL
    # =========================================

    queixa_principal = models.TextField(
        blank=True
    )

    # =========================================
    # HISTÓRIA MÉDICA
    # =========================================

    hipertenso = models.BooleanField(
        default=False
    )

    diabetico = models.BooleanField(
        default=False
    )

    cardiopatia = models.BooleanField(
        default=False
    )

    asma = models.BooleanField(
        default=False
    )

    bronquite = models.BooleanField(
        default=False
    )

    anemia = models.BooleanField(
        default=False
    )

    hepatite = models.BooleanField(
        default=False
    )

    rinite = models.BooleanField(
        default=False
    )

    sinusite = models.BooleanField(
        default=False
    )

    problema_renal = models.BooleanField(
        default=False
    )

    sangramento_excessivo = models.BooleanField(
        default=False
    )    

    alergico = models.BooleanField(
        default=False
    )

    alergias = models.TextField(
        blank=True
    )

    fumante = models.BooleanField(
        default=False
    )

    gravida = models.BooleanField(
        default=False
    )

    historico_medico = models.TextField(
        blank=True
    )

    # =========================================
    # MEDICAMENTOS
    # =========================================

    usa_medicamento = models.BooleanField(
        default=False
    )

    medicamentos = models.TextField(
        blank=True
    )

    antibioticos = models.TextField(
        blank=True
    )

    antiinflamatorios = models.TextField(
        blank=True
    )

    analgesicos = models.TextField(
        blank=True
    )

    # =========================================
    # CIRURGIAS / HOSPITALIZAÇÃO
    # =========================================

    cirurgia = models.BooleanField(
        default=False
    )

    cirurgias = models.TextField(
        blank=True
    )

    hospitalizado = models.BooleanField(
        default=False
    )

    hospitalizacao = models.TextField(
        blank=True
    )

    transfusao_sangue = models.BooleanField(
        default=False
    )

    # =========================================
    # CONDIÇÕES MÉDICAS IMPORTANTES
    # =========================================

    anticoagulante = models.BooleanField(
        default=False
    )

    bisfosfonato = models.BooleanField(
        default=False
    )

    marcapasso = models.BooleanField(
        default=False
    )

    cancer = models.BooleanField(
        default=False
    )

    hipotireoidismo = models.BooleanField(
        default=False
    )

    hipertireoidismo = models.BooleanField(
        default=False
    )

    # =========================================
    # HISTÓRIA ODONTOLÓGICA
    # =========================================

    primeira_consulta = models.BooleanField(
        default=False
    )

    ultima_consulta = models.DateField(
        null=True,
        blank=True
    )

    experiencia_odontologica = models.TextField(
        blank=True
    )

    abandono_tratamento = models.BooleanField(
        default=False
    )

    medo_dentista = models.BooleanField(
        default=False
    )

    anestesia_reacao = models.TextField(
        blank=True
    )

    sangramento_gengival = models.BooleanField(
        default=False
    )

    sensibilidade = models.BooleanField(
        default=False
    )

    dor_mastigar = models.BooleanField(
        default=False
    )

    # =========================================
    # HIGIENE ORAL
    # =========================================

    frequencia_escovacao = models.CharField(
        max_length=100,
        blank=True
    )

    usa_fio_dental = models.BooleanField(
        default=False
    )

    usa_enxaguante = models.BooleanField(
        default=False
    )

    escova_lingua = models.BooleanField(
        default=False
    )

    # =========================================
    # HÁBITOS
    # =========================================

    bruxismo = models.BooleanField(
        default=False
    )

    ronco = models.BooleanField(
        default=False
    )

    respiracao_bucal = models.BooleanField(
        default=False
    )

    roer_unhas = models.BooleanField(
        default=False
    )

    morde_objetos = models.BooleanField(
        default=False
    )

    chupeta = models.BooleanField(
        default=False
    )

    succao_dedo = models.BooleanField(
        default=False
    )

    baba_travesseiro = models.BooleanField(
        default=False
    )

    dorme_boca_aberta = models.BooleanField(
        default=False
    )

    morde_labios = models.BooleanField(
        default=False
    )

    # =========================================
    # HÁBITOS ALIMENTARES
    # =========================================

    belisca_refeicoes = models.BooleanField(
        default=False
    )

    alimentacao_cariogenica = models.BooleanField(
        default=False
    )

    tipo_alimentacao = models.CharField(
        max_length=100,
        blank=True
    )

    # =========================================
    # PERFIL COMPORTAMENTAL
    # =========================================

    ansioso = models.BooleanField(
        default=False
    )

    agitado = models.BooleanField(
        default=False
    )

    calmo = models.BooleanField(
        default=False
    )

    comunicativo = models.BooleanField(
        default=False
    )

    retraido = models.BooleanField(
        default=False
    )
    introvertido = models.BooleanField(
        default=False
    )

    extrovertido = models.BooleanField(
        default=False
    )

    # =========================================
    # OBSERVAÇÕES
    # =========================================

    observacoes = models.TextField(
        blank=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return f'Anamnese - {self.paciente.nome}'
    
# =========================================
# PROCEDIMENTOS
# =========================================

class Procedimento(models.Model):

    # =========================================
    # CATEGORIAS
    # =========================================

    CATEGORIAS = [
        ('diagnostico', 'Diagnóstico'),
        ('dentistica', 'Dentística'),
        ('endodontia', 'Endodontia'),
        ('periodontia', 'Periodontia'),
        ('cirurgia', 'Cirurgia'),
        ('protese', 'Prótese'),
        ('implantodontia', 'Implantodontia'),
        ('ortodontia', 'Ortodontia'),
        ('geral', 'Geral')

    ]

    # =========================================
    # TIPOS
    # =========================================

    TIPOS = [

        ('dente', 'Por Dente'),
        ('hemiarcada', 'Hemi-Arcada'),
        ('geral', 'Geral'),
        ('cirurgia', 'Cirurgia')

    ]

    # =========================================
    # POSIÇÕES
    # =========================================

    POSICOES = [

        ('coroa', 'Coroa'),
        ('raiz', 'Raiz'),
        ('oclusal', 'Oclusal'),
        ('vestibular', 'Vestibular'),
        ('lingual', 'Lingual'),
        ('centro', 'Centro')

    ]

    # =========================================
    # STATUS CLÍNICO
    # =========================================

    STATUS = [

        ('realizar', 'A Realizar'),
        ('andamento', 'Em Andamento'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado'),
        ('reavaliar', 'Reavaliar')

    ]

    # =========================================
    # NOME
    # =========================================

    nome = models.CharField(

        max_length=255

    )

    # =========================================
    # CATEGORIA
    # =========================================

    categoria = models.CharField(

        max_length=100,

        choices=CATEGORIAS,

        default='geral'

    )

    # =========================================
    # TIPO
    # =========================================

    tipo = models.CharField(

        max_length=50,

        choices=TIPOS,

        default='dente'

    )

    # =========================================
    # STATUS
    # =========================================

    status = models.CharField(

        max_length=30,

        choices=STATUS,

        default='realizar'

    )

    # =========================================
    # ÍCONE ANTIGO
    # =========================================

    icone = models.CharField(

        max_length=100,

        blank=True,

        null=True

    )

    # =========================================
    # NOVO ARQUIVO DO ÍCONE
    # =========================================

    arquivo_icone = models.CharField(

        max_length=255,

        blank=True,

        null=True

    )

    # =========================================
    # POSIÇÃO DO ÍCONE
    # =========================================

    posicao_icone = models.CharField(

        max_length=30,

        choices=POSICOES,

        default='centro'

    )

    # =========================================
    # VALOR PARTICULAR
    # =========================================

    valor_particular = models.DecimalField(

        max_digits=10,

        decimal_places=2,

        default=0

    )

    # =========================================
    # VALOR CONVÊNIO
    # =========================================

    valor_convenio = models.DecimalField(

        max_digits=10,

        decimal_places=2,

        default=0

    )

    # =========================================
    # TEMPO ESTIMADO
    # =========================================

    tempo_estimado = models.IntegerField(

        default=60,

        help_text='Tempo em minutos'

    )

    # =========================================
    # CUSTO CLÍNICO
    # =========================================

    custo_clinico = models.DecimalField(

        max_digits=10,

        decimal_places=2,

        default=0

    )

    # =========================================
    # ATIVO
    # =========================================

    ativo = models.BooleanField(

        default=True

    )

    # =========================================
    # ORDEM
    # =========================================

    ordem = models.IntegerField(

        default=0

    )

    # =========================================
    # DATA
    # =========================================

    criado_em = models.DateTimeField(

        auto_now_add=True

    )

    # =========================================
    # META
    # =========================================

    class Meta:

        ordering = ['categoria', 'ordem', 'nome']

        verbose_name = 'Procedimento'

        verbose_name_plural = 'Procedimentos'

    # =========================================
    # STRING
    # =========================================

    def __str__(self):

        return self.nome



# =========================================
# EVOLUÇÃO CLÍNICA
# =========================================

class EvolucaoClinica(models.Model):

    STATUS_CHOICES = (

        ('existente', 'Existente'),
        ('planejado', 'Planejado'),
        ('andamento', 'Em Andamento'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado'),

    )

        # =========================================
    # PACIENTE
    # =========================================

    paciente = models.ForeignKey(

        Paciente,

        on_delete=models.CASCADE,

        related_name='evolucoes'

    )

    # =========================================
    # TRATAMENTO
    # =========================================

    tratamento = models.ForeignKey(

        'Tratamento',

        on_delete=models.CASCADE,

        related_name='evolucoes',

        null=True,

        blank=True

    )

    
    # =========================================
    # ORÇAMENTO
    # =========================================

    orcamento = models.ForeignKey(

        'Orcamento',

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name='evolucoes'

    )

    # =========================================
    # ITEM DO ORÇAMENTO
    # =========================================

    item_orcamento = models.ForeignKey(

        'ItemOrcamento',

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name='evolucoes'

    )

    # =========================================
    # DENTE
    # =========================================

    dente = models.CharField(

        max_length=10,

        blank=True,

        null=True

    )

    # =========================================
    # FACE
    # =========================================

    face = models.CharField(

        max_length=20,

        blank=True,

        null=True

    )

    # =========================================
    # POSIÇÃO DO ÍCONE
    # =========================================

    posicao_icone = models.CharField(

        max_length=20,

        blank=True,

        null=True,

        choices=Procedimento.POSICOES

    )

    # =========================================
    # PROCEDIMENTO
    # =========================================

    procedimento = models.ForeignKey(

        Procedimento,

        on_delete=models.SET_NULL,

        null=True,

        blank=True

    )

    # =========================================
    # STATUS
    # =========================================

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default='planejado'

    )

    # =========================================
    # DESCRIÇÃO
    # =========================================

    descricao = models.TextField(

        blank=True,

        null=True

    )

    # =========================================
    # DATA
    # =========================================

    criado_em = models.DateTimeField(

        auto_now_add=True

    )

    class Meta:

        ordering = ['-criado_em']

    def __str__(self):

        procedimento = (

            self.procedimento.nome

            if self.procedimento

            else 'Sem procedimento'

        )

        return (

            f'{self.paciente.nome} - '

            f'{procedimento} - '

            f'{self.get_status_display()}'

        )



# =========================================
# PRONTUÁRIO CLÍNICO
# =========================================

class ProntuarioClinico(models.Model):

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name='prontuarios'
    )

    titulo = models.CharField(
        max_length=200
    )

    anotacao = models.TextField()

    dente = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    procedimento = models.ForeignKey(
        Procedimento,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    descricao = models.TextField(
        blank=True
    )

    materiais = models.TextField(
        blank=True
    )

    anestesia = models.CharField(
        max_length=255,
        blank=True
    )

    retorno = models.DateField(
        null=True,
        blank=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ['-criado_em']

        verbose_name = 'Prontuário Clínico'

        verbose_name_plural = 'Prontuários Clínicos'

    def __str__(self):

        if self.procedimento:

            return (
                f'{self.paciente.nome} - '
                f'{self.procedimento.nome}'
            )

        return (
            f'{self.paciente.nome} - '
            f'{self.titulo}'
        )
    
# =========================================
# TRATAMENTO
# =========================================

class Tratamento(models.Model):

    STATUS_CHOICES = [
        ("ATIVO", "Ativo"),
        ("ENCERRADO", "Encerrado"),
    ]

    # =========================================
    # PACIENTE
    # =========================================

    paciente = models.ForeignKey(
        "Paciente",
        on_delete=models.CASCADE,
        related_name="tratamentos"
    )

    # =========================================
    # DENTISTA RESPONSÁVEL
    # =========================================

    dentista = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pacientes"
    )

    # =========================================
    # TÍTULO
    # =========================================

    titulo = models.CharField(
        "Título",
        max_length=150,
        default="Tratamento Inicial"
    )

    # =========================================
    # STATUS
    # =========================================

    status = models.CharField(
        "Status",
        max_length=15,
        choices=STATUS_CHOICES,
        default="ATIVO"
    )

    # =========================================
    # DATA DE INÍCIO
    # =========================================

    data_inicio = models.DateField(
        "Data de início",
        default=timezone.now
    )

    # =========================================
    # DATA DE ENCERRAMENTO
    # =========================================

    data_encerramento = models.DateField(
        "Data de encerramento",
        null=True,
        blank=True
    )

    # =========================================
    # OBSERVAÇÕES
    # =========================================

    observacoes = models.TextField(
        "Observações",
        blank=True
    )

    # =========================================
    # CONTROLE
    # =========================================

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name = "Tratamento"
        verbose_name_plural = "Tratamentos"
        ordering = ["-criado_em"]

    # =========================================
    # SAVE
    # =========================================

    def save(self, *args, **kwargs):

        """
        Regras do tratamento:

        - Apenas um tratamento ativo por paciente.
        - O dentista responsável deve ser informado na criação
        do tratamento.
        """

        # Garante apenas um tratamento ativo por paciente.

        if self.status == "ATIVO":

            Tratamento.objects.filter(
                paciente=self.paciente,
                status="ATIVO"
            ).exclude(
                pk=self.pk
            ).update(
                status="ENCERRADO",
                data_encerramento=timezone.now().date()
            )

        super().save(*args, **kwargs)

    # =========================================
    # STRING
    # =========================================

    def __str__(self):

        return f"{self.paciente.nome} - {self.titulo}"

# =========================================
# POSIÇÕES CLÍNICAS DO DENTE
# =========================================

POSICOES_DENTE = (

    ('normal', 'Normal'),

    ('incluso_vertical', 'Inclusão vertical'),

    ('incluso_horizontal', 'Inclusão horizontal'),

    ('incluso_mesial', 'Inclusão mesial'),

    ('incluso_distal', 'Inclusão distal'),

    ('inclinado_direita', 'Inclinado para direita'),

    ('inclinado_esquerda', 'Inclinado para esquerda'),

    ('rotacao', 'Rotação / Giro'),

    ('extrusao', 'Extrusão'),

)

# =========================================
# POSICIONAMENTO DO DENTE
# =========================================

class PosicionamentoDente(models.Model):

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name="posicionamentos_dentes"
    )

    dente = models.CharField(
        max_length=2
    )

    posicao = models.CharField(
        max_length=30,
        choices=POSICOES_DENTE,
        default="normal"
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name = "Posicionamento do Dente"
        verbose_name_plural = "Posicionamentos dos Dentes"

        constraints = [
            models.UniqueConstraint(
                fields=["paciente", "dente"],
                name="unique_posicionamento_dente_paciente"
            )
        ]

    def __str__(self):

        return (
            f"{self.paciente.nome} - "
            f"Dente {self.dente} - "
            f"{self.posicao}"
        )
    
    
# =========================================
# ORÇAMENTO
# =========================================

class Orcamento(models.Model):

    # =========================================
    # PACIENTE
    # =========================================

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name="orcamentos"
    )

    # =========================================
    # TRATAMENTO
    # =========================================

    tratamento = models.ForeignKey(
        Tratamento,
        on_delete=models.CASCADE,
        related_name="orcamentos",
        null=True,
        blank=True
    )

    # =========================================
    # STATUS
    # =========================================

    STATUS_CHOICES = (

        ("rascunho", "Rascunho"),
        ("aprovado", "Aprovado"),
        ("em_execucao", "Em Execução"),
        ("finalizado", "Finalizado"),
        ("cancelado", "Cancelado"),

    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="rascunho"
    )

    # =========================================
    # NEGOCIAÇÃO
    # =========================================

    desconto = models.DecimalField(
        "Desconto",
        max_digits=10,
        decimal_places=2,
        default=0
    )

    acrescimo = models.DecimalField(
        "Acréscimo",
        max_digits=10,
        decimal_places=2,
        default=0
    )

    # =========================================
    # PAGAMENTO
    # =========================================

    entrada = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    parcelas = models.PositiveIntegerField(
        default=1
    )

    FORMA_PAGAMENTO = (

        ("dinheiro", "Dinheiro"),
        ("pix", "PIX"),
        ("debito", "Cartão Débito"),
        ("credito", "Cartão Crédito"),
        ("boleto", "Boleto"),

    )

    forma_pagamento = models.CharField(
        max_length=20,
        choices=FORMA_PAGAMENTO,
        default="pix"
    )

    # =========================================
    # OBSERVAÇÕES
    # =========================================

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    # =========================================
    # CONTROLE
    # =========================================

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    # =========================================
    # SUBTOTAL
    # =========================================

    @property
    def subtotal(self):

        return sum(
            (
                item.total
                for item in self.itens.all()
                if item.status != "cancelado"
            ),
            Decimal("0.00")
        )


    # =========================================
    # VERIFICA SE POSSUI ITENS ATIVOS
    # =========================================

    @property
    def tem_itens_ativos(self):

        return self.itens.exclude(
            status="cancelado"
        ).exists()

    # =========================================
    # VALOR DO DESCONTO
    # =========================================

    @property
    def valor_desconto(self):

        valor = (
            self.subtotal *
            (self.desconto or Decimal("0.00"))
        ) / Decimal("100")

        return valor.quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

    # =========================================
    # VALOR DO ACRÉSCIMO
    # =========================================

    @property
    def valor_acrescimo(self):

        valor = (
            self.subtotal *
            (self.acrescimo or Decimal("0.00"))
        ) / Decimal("100")

        return valor.quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

    # =========================================
    # TOTAL BRUTO
    # =========================================

    @property
    def total_bruto(self):

        return self.subtotal

    # =========================================
    # TOTAL LÍQUIDO
    # =========================================

    @property
    def total(self):

        total = (
            self.subtotal
            - self.valor_desconto
            + self.valor_acrescimo
        )

        return max(
            total,
            Decimal("0.00")
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

    # =========================================
    # SALDO A RECEBER
    # =========================================

    @property
    def saldo(self):

        saldo = self.total - (self.entrada or Decimal("0.00"))

        return max(
            saldo,
            Decimal("0.00")
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )
    # =========================================
    # QUANTIDADE DE ITENS
    # =========================================

    @property
    def quantidade_itens(self):

        return self.itens.count()

    # =========================================
    # VALOR DA PARCELA
    # =========================================

    @property
    def valor_parcela(self):

        if not self.parcelas or self.parcelas <= 0:
            return self.saldo

        return (
            self.saldo / Decimal(str(self.parcelas))
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

    # =========================================
    # STRING
    # =========================================

    def __str__(self):

        return (
            f"Orçamento #{self.id} - "
            f"{self.paciente.nome}"
        )
            
# =========================================
# CONFIGURAÇÃO DA CLÍNICA
# =========================================

class ConfiguracaoClinica(models.Model):

    nome_clinica = models.CharField(
        max_length=200
    )

    logo = models.ImageField(
        upload_to='clinica/',
        blank=True,
        null=True
    )

    cro = models.CharField(
        max_length=50,
        blank=True
    )

    cnpj = models.CharField(
        max_length=30,
        blank=True
    )

    telefone = models.CharField(
        max_length=30,
        blank=True
    )

    whatsapp = models.CharField(
        max_length=30,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    endereco = models.CharField(
        max_length=255,
        blank=True
    )

    numero = models.CharField(
        max_length=20,
        blank=True
    )

    bairro = models.CharField(
        max_length=100,
        blank=True
    )

    cidade = models.CharField(
        max_length=100,
        blank=True
    )

    estado = models.CharField(
        max_length=2,
        blank=True
    )

    cep = models.CharField(
        max_length=20,
        blank=True
    )

    observacoes_orcamento = models.TextField(
        blank=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name = 'Configuração da Clínica'

        verbose_name_plural = (
            'Configurações da Clínica'
        )

    def __str__(self):

        return self.nome_clinica

# =========================================
# CONVÊNIOS
# =========================================

class Convenio(models.Model):

    nome = models.CharField(

        max_length=150

    )

    indice = models.DecimalField(

        max_digits=5,
        decimal_places=2,
        default=1.00

    )

    telefone = models.CharField(

        max_length=20,
        blank=True,
        null=True

    )

    observacoes = models.TextField(

        blank=True,
        null=True

    )

    ativo = models.BooleanField(

        default=True

    )

    criado_em = models.DateTimeField(

        auto_now_add=True

    )

    def __str__(self):

        return self.nome
  

# =========================================
# ITEM ORÇAMENTO
# =========================================

TIPO_LOCAL = (

    ('dente', 'Dente'),
    ('hemiarcada', 'Hemi Arcada'),
    ('geral', 'Geral'),

)


HEMI_CHOICES = (

    ('sup_dir', 'Superior Direita'),
    ('sup_esq', 'Superior Esquerda'),
    ('inf_dir', 'Inferior Direita'),
    ('inf_esq', 'Inferior Esquerda'),

)


class ItemOrcamento(models.Model):
    STATUS_CHOICES = (

        ('existente', 'Existente'),
        ('planejado', 'Planejado'),
        ('andamento', 'Em Andamento'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado'),

    )

  

    # =========================================
    # ORÇAMENTO
    # =========================================

    orcamento = models.ForeignKey(

        Orcamento,

        on_delete=models.CASCADE,

        related_name='itens'

    )


    # =========================================
    # PROCEDIMENTO
    # =========================================

    procedimento = models.ForeignKey(

        Procedimento,

        on_delete=models.SET_NULL,

        null=True

    )

    # =========================================
    # TIPO LOCAL
    # =========================================

    tipo_local = models.CharField(

        max_length=20,

        choices=TIPO_LOCAL,

        default='dente'

    )

    # =========================================
    # DENTE
    # =========================================

    dente = models.CharField(

        max_length=10,

        blank=True,

        null=True

    )

    # =========================================
    # FACE
    # =========================================

    face = models.CharField(

        max_length=10,

        blank=True,

        null=True

    )

    # =========================================
    # POSIÇÃO DO ÍCONE
    # =========================================

    posicao_icone = models.CharField(

        max_length=20,

        blank=True,

        null=True,

        choices=Procedimento.POSICOES

    )

    
    # =========================================
    # HEMI ARCADA
    # =========================================

    hemi_arcada = models.CharField(

        max_length=20,

        choices=HEMI_CHOICES,

        blank=True,

        null=True

    )


    # =========================================
    # QUANTIDADE
    # =========================================

    quantidade = models.IntegerField(

        default=1

    )

    # =========================================
    # VALOR
    # =========================================

    valor_unitario = models.DecimalField(

        max_digits=10,

        decimal_places=2,

        default=0

    )

    # =========================================
    # STATUS
    # =========================================

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default='planejado'

    )

    # =========================================
    # TOTAL
    # =========================================

    @property
    def total(self):

        return self.quantidade * self.valor_unitario

    # =========================================
    # STRING
    # =========================================

    def __str__(self):

        procedimento = (
            self.procedimento.nome
            if self.procedimento
            else 'Procedimento'
        )

        return f'{procedimento} - {self.orcamento.paciente.nome}'
    
# =========================================
# ANEXOS PACIENTE
# =========================================

class AnexoPaciente(models.Model):

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name='anexos'
    )

    TIPO_CHOICES = (

        ('foto', 'Foto Clínica'),
        ('radiografia', 'Radiografia'),
        ('tomografia', 'Tomografia'),
        ('documento', 'Documento'),
        ('exame', 'Exame')

    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        default='documento'
    )

    descricao = models.CharField(
        max_length=200
    )

    arquivo = models.FileField(
        upload_to='anexos_pacientes/'
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ['-criado_em']

    def __str__(self):

        return (
            f'{self.paciente.nome} - '
            f'{self.descricao}'
        )
    
# =========================================
# TEMPLATES DOCUMENTOS
# =========================================

class TemplateDocumento(models.Model):

    TIPO_CHOICES = (

        ('atestado', 'Atestado Odontológico'),
        ('declaracao', 'Declaração de Comparecimento'),
        ('receita', 'Receituário Simples'),
        ('controle_especial', 'Receituário Controle Especial'),
        ('exames', 'Solicitação de Exames'),
        ('encaminhamento', 'Encaminhamento'),
        ('relatorio', 'Relatório Odontológico'),
        ('alta', 'Termo de Alta'),
        ('consentimento', 'Termo de Consentimento'),
        ('contrato', 'Contrato'),
        ('livre', 'Documento Livre'),

    )

    nome = models.CharField(
        max_length=200
    )

    tipo = models.CharField(
        max_length=30,
        choices=TIPO_CHOICES
    )

    conteudo = models.TextField()

    ativo = models.BooleanField(
        default=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.nome
    
# =========================================
# DOCUMENTOS CLÍNICOS
# =========================================

class DocumentoClinico(models.Model):

    STATUS = (

        ('rascunho', 'Rascunho'),
        ('finalizado', 'Finalizado'),

    )

    TIPOS = (

        ('atestado', 'Atestado Odontológico'),

        ('declaracao', 'Declaração de Comparecimento'),

        ('receita', 'Receituário Simples'),

        ('controle_especial', 'Receituário Controle Especial'),

        ('exames', 'Solicitação de Exames'),

        ('encaminhamento', 'Encaminhamento'),

        ('relatorio', 'Relatório Odontológico'),

        ('alta', 'Termo de Alta'),

        ('consentimento', 'Termo de Consentimento'),

        ('contrato', 'Contrato'),

        ('personalizado', 'Documento Personalizado'),

    )

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name='documentos'
    )

    template = models.ForeignKey(
        TemplateDocumento,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    titulo = models.CharField(
        max_length=255
    )

    tipo = models.CharField(
        max_length=30,
        choices=TIPOS,
        default='personalizado'
    )

    conteudo = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='rascunho'
    )

    pdf = models.FileField(
        upload_to='documentos/',
        blank=True,
        null=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ['-criado_em']

        verbose_name = 'Documento Clínico'

        verbose_name_plural = 'Documentos Clínicos'

    def __str__(self):

        return f'{self.titulo} - {self.paciente.nome}'
    
   
# =========================================
# MEDICAMENTOS
# =========================================

class Medicamento(models.Model):

    CATEGORIAS = (

        ('antibiotico', 'Antibiótico'),
        ('analgesico', 'Analgésico'),
        ('antiinflamatorio', 'Anti-inflamatório'),
        ('antisseptico', 'Antisséptico'),
        ('outro', 'Outro'),

    )

    nome = models.CharField(
        max_length=200
    )

    concentracao = models.CharField(
        max_length=100,
        blank=True
    )

    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIAS,
        default='outro'
    )

    ativo = models.BooleanField(
        default=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        if self.concentracao:

            return (
                f'{self.nome} '
                f'{self.concentracao}'
            )

        return self.nome


# =========================================
# RECEITAS
# =========================================

class Receita(models.Model):


    paciente = models.ForeignKey(

        Paciente,

        on_delete=models.CASCADE,

        related_name='receitas'

    )

    medicamento = models.CharField(

        max_length=300

    )

    titulo = models.CharField(

        max_length=200,

        default='Receituário'

    )

    quantidade = models.CharField(

        max_length=100

    )

    posologia = models.TextField()

    observacoes = models.TextField(

        blank=True,

        null=True

    )

    TIPO_RECEITA = (

        ('simples', 'Receituário Simples'),

        ('controle', 'Receita de Controle Especial'),

    )

    tipo_receita = models.CharField(

        max_length=20,

        choices=TIPO_RECEITA,

        default='simples'

    )

    status = models.CharField(

        max_length=20,

        default='ativo'

    )

    criado_em = models.DateTimeField(

        auto_now_add=True

    )

    class Meta:

        ordering = ['-criado_em']

    def __str__(self):

        return (
            f'{self.paciente.nome} - '
            f'{self.medicamento}'
        )
    

# =========================================
# MODELOS DE RECEITA
# =========================================

class ModeloReceita(models.Model):

    nome = models.CharField(
        max_length=200
    )

    medicamento = models.CharField(
        max_length=255
    )

    quantidade = models.CharField(
        max_length=100,
        blank=True
    )

    posologia = models.TextField()

    ativo = models.BooleanField(
        default=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        verbose_name = 'Modelo de Receita'

        verbose_name_plural = 'Modelos de Receita'

        ordering = ['nome']

    def __str__(self):

        return self.nome
    

# =========================================
# EXAMES
# =========================================

class Exame(models.Model):

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name='exames'
    )

    nome = models.CharField(
        max_length=200
    )

    data_exame = models.DateField(
        blank=True,
        null=True
    )

    arquivo = models.FileField(
        upload_to='exames/',
        blank=True,
        null=True
    )

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ['-criado_em']

        verbose_name = 'Exame'

        verbose_name_plural = 'Exames'

    def __str__(self):

        return (
            f'{self.paciente.nome} - '
            f'{self.nome}'
        )
    
# =========================================
# SOLICITAÇÃO DE EXAMES
# =========================================

class SolicitacaoExame(models.Model):

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name='solicitacoes_exames'
    )

    titulo = models.CharField(
        max_length=200
    )

    exames_solicitados = models.TextField()

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ['-criado_em']

        verbose_name = 'Solicitação de Exame'

        verbose_name_plural = 'Solicitações de Exames'

    def __str__(self):

        return (
            f'{self.paciente.nome} - '
            f'{self.titulo}'
        )
    

# =========================================
# PERFIS
# =========================================

class Perfil(models.Model):

    OPERACIONAL = "operacional"
    ADMINISTRATIVO = "administrativo"

    TIPOS_PERFIL = [

        (OPERACIONAL, "Operacional"),
        (ADMINISTRATIVO, "Administrativo"),

    ]

    nome = models.CharField(
        "Nome",
        max_length=100,
        unique=True
    )

    tipo = models.CharField(
        "Tipo do Perfil",
        max_length=20,
        choices=TIPOS_PERFIL,
        default=OPERACIONAL
    )

    descricao = models.TextField(
        "Descrição",
        blank=True,
        null=True
    )

    ativo = models.BooleanField(
        "Ativo",
        default=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ["tipo", "nome"]

        verbose_name = "Perfil"

        verbose_name_plural = "Perfis"

    def __str__(self):

        return self.nome

    @property
    def is_administrativo(self):

        return self.tipo == self.ADMINISTRATIVO

    @property
    def is_operacional(self):

        return self.tipo == self.OPERACIONAL
    
# =========================================
# MÓDULOS DO SISTEMA
# =========================================

from django.db import models
from django.utils import timezone


class Modulo(models.Model):

    codigo = models.CharField(
        "Código",
        max_length=50,
        unique=True
    )

    nome = models.CharField(
        "Nome",
        max_length=100
    )

    grupo = models.CharField(
        "Grupo",
        max_length=50,
        default="GERAL"
    )

    icone = models.CharField(
        "Ícone",
        max_length=50,
        blank=True,
        default=""
    )

    ordem = models.PositiveIntegerField(
        "Ordem",
        default=0
    )

    ativo = models.BooleanField(
        "Ativo",
        default=True
    )

    criado_em = models.DateTimeField(
        "Criado em",
        default=timezone.now,
        editable=False
    )

    atualizado_em = models.DateTimeField(
        "Atualizado em",
        auto_now=True
    )

    class Meta:

        ordering = ["grupo", "ordem", "nome"]

        verbose_name = "Módulo"

        verbose_name_plural = "Módulos"

    def __str__(self):

        return f"{self.grupo} - {self.nome}"
    
# =========================================
# PERFIL DE USUÁRIO
# =========================================

class PerfilUsuario(models.Model):

    usuario = models.OneToOneField(

        User,

        on_delete=models.CASCADE,

        related_name="perfil"

    )

    perfil_acesso = models.ForeignKey(

        Perfil,

        on_delete=models.PROTECT,

        related_name="usuarios",

        verbose_name="Perfil de Acesso",

        blank=True,

        null=True

    )

    ADMIN = "admin"
    GESTOR = "gestor"
    DENTISTA = "dentista"
    SECRETARIA = "secretaria"
    ACD = "acd"
    CONTABILIDADE = "contabilidade"
    MARKETING = "marketing"
    AUDITORIA = "auditoria"

    TIPOS_USUARIO = [

        (ADMIN, "Administrador"),

        (GESTOR, "Gestor"),

        (DENTISTA, "Dentista"),

        (SECRETARIA, "Secretária"),

        (ACD, "Auxiliar de Saúde Bucal"),

        (CONTABILIDADE, "Contabilidade"),

        (MARKETING, "Marketing"),

        (AUDITORIA, "Auditoria"),

    ]

    tipo_usuario = models.CharField(

        max_length=30,

        choices=TIPOS_USUARIO,

        default=SECRETARIA

    )

        # =========================================
    # DADOS PROFISSIONAIS
    # =========================================

    cro = models.CharField(

        max_length=20,

        blank=True,

        null=True

    )

    especialidade = models.CharField(

        max_length=100,

        blank=True,

        null=True

    )
    # =========================================
    # COMISSÃO
    # =========================================

    percentual_comissao = models.DecimalField(

        "Comissão (%)",

        max_digits=5,

        decimal_places=2,

        default=40.00,

        help_text="Percentual de comissão do dentista."

    )

    # =========================================
    # META MENSAL
    # =========================================

    meta_mensal = models.DecimalField(

        "Meta Mensal (R$)",

        max_digits=10,

        decimal_places=2,

        default=0.00,

        help_text="Meta mensal de produção do dentista."

    )

    telefone = models.CharField(

        max_length=20,

        blank=True,

        null=True

    )

    celular = models.CharField(

        max_length=20,

        blank=True,

        null=True

    )
    
    # =========================================
    # DADOS PESSOAIS
    # =========================================

    cpf = models.CharField(

        max_length=14,

        blank=True,

        null=True

    )

    rg = models.CharField(

        max_length=20,

        blank=True,

        null=True

    )

    data_nascimento = models.DateField(

        blank=True,

        null=True

    )

    sexo = models.CharField(

        max_length=20,

        blank=True,

        null=True

    )

    foto = models.ImageField(

        upload_to="usuarios/fotos/",

        blank=True,

        null=True

    )

    assinatura = models.ImageField(

        upload_to="usuarios/assinaturas/",

        blank=True,

        null=True

    )

    # =========================================
    # ENDEREÇO
    # =========================================

    cep = models.CharField(

        max_length=10,

        blank=True,

        null=True

    )

    logradouro = models.CharField(

        max_length=255,

        blank=True,

        null=True

    )

    numero = models.CharField(

        max_length=20,

        blank=True,

        null=True

    )

    complemento = models.CharField(

        max_length=100,

        blank=True,

        null=True

    )

    bairro = models.CharField(

        max_length=100,

        blank=True,

        null=True

    )

    cidade = models.CharField(

        max_length=100,

        blank=True,

        null=True

    )

    uf = models.CharField(

        max_length=2,

        blank=True,

        null=True

    )

    # =========================================
    # CRO
    # =========================================

    cro_uf = models.CharField(

        max_length=2,

        blank=True,

        null=True

    )

    # =========================================
    # CONTROLE
    # =========================================

    ativo = models.BooleanField(

        default=True

    )

    somente_leitura = models.BooleanField(

        default=False

    )

    criado_em = models.DateTimeField(

        auto_now_add=True

    )

    atualizado_em = models.DateTimeField(

        auto_now=True

    )

    def __str__(self):

        nome = self.usuario.get_full_name()

        if nome:

            return f"{nome} ({self.get_tipo_usuario_display()})"

        return f"{self.usuario.username} ({self.get_tipo_usuario_display()})"

    
# =========================================
# FORNECEDORES
# =========================================

class Fornecedor(models.Model):

    nome = models.CharField(
        max_length=200
    )

    razao_social = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    cnpj = models.CharField(
        max_length=18,
        blank=True,
        null=True,
        db_index=True
    )

    contato = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    telefone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    celular = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    # Endereço

    cep = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    logradouro = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    numero = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    complemento = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    bairro = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    cidade = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    uf = models.CharField(
        max_length=2,
        blank=True,
        null=True
    )

    # Controle

    ativo = models.BooleanField(
        default=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.nome
    

# =========================================
# PRODUTOS
# =========================================

class Produto(models.Model):

    nome = models.CharField(
        max_length=200
    )

    descricao = models.TextField(
        blank=True,
        null=True
    )

    codigo = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    estoque = models.IntegerField(
        default=0
    )

    estoque_minimo = models.IntegerField(
        default=0
    )

    valor_compra = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    valor_venda = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    ativo = models.BooleanField(
        default=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['nome']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):

        return self.nome

    @property
    def estoque_critico(self):

        return self.estoque <= self.estoque_minimo

    @staticmethod
    def produtos_criticos():

        return Produto.objects.filter(
            estoque__lte=F('estoque_minimo'),
            ativo=True
        )

    def entrada_estoque(self, quantidade):

        self.estoque += quantidade
        self.save()

    def saida_estoque(self, quantidade):

        if quantidade > self.estoque:
            raise ValueError(
                'Estoque insuficiente.'
            )

        self.estoque -= quantidade
        self.save()    

# =========================================
# COMPRAS
# =========================================

class Compra(models.Model):

    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.PROTECT
    )

    data_compra = models.DateField()

    numero_nf = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    arquivo_nf = models.FileField(
        upload_to='notas_fiscais/',
        blank=True,
        null=True
    )

    valor_total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f'Compra #{self.id}'    

# =========================================
# ITENS DA COMPRA
# =========================================

class ItemCompra(models.Model):

    compra = models.ForeignKey(
        Compra,
        on_delete=models.CASCADE,
        related_name='itens'
    )

    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT
    )

    quantidade = models.PositiveIntegerField()

    valor_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    def save(self, *args, **kwargs):

        self.subtotal = (
            self.quantidade *
            self.valor_unitario
        )

        super().save(*args, **kwargs)

    def __str__(self):

        return (
            f'{self.produto.nome} '
            f'({self.quantidade})'
        )
    

# =========================================
# MOVIMENTAÇÃO DO ESTOQUE
# =========================================

class MovimentacaoEstoque(models.Model):

    TIPO_CHOICES = [
        ('COMPRA', 'Compra'),
        ('ENTRADA', 'Entrada'),
        ('SAIDA', 'Saída'),
        ('AJUSTE', 'Ajuste'),
    ]

    produto = models.ForeignKey(
        'Produto',
        on_delete=models.PROTECT,
        related_name='movimentacoes'
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES
    )

    quantidade = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    estoque_anterior = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    estoque_atual = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    observacao = models.TextField(
        blank=True,
        null=True
    )

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='movimentacoes_estoque'
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Movimentação de Estoque'
        verbose_name_plural = 'Movimentações de Estoque'
        ordering = ['-criado_em']

    def __str__(self):

        return (
            f'{self.produto.nome} - '
            f'{self.tipo} - '
            f'{self.quantidade}'
        )
    

# =========================================
# LOTES DE PRODUTOS
# =========================================

class LoteProduto(models.Model):

    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name='lotes'
    )

    lote = models.CharField(
        max_length=50
    )

    quantidade = models.IntegerField(
        default=0
    )

    validade = models.DateField()

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = [

            'validade'

        ]

        verbose_name = 'Lote'

        verbose_name_plural = 'Lotes'

    def __str__(self):

        return (

            f'{self.produto.nome} - '

            f'{self.lote}'

        )


# =========================================
# CONTAS A PAGAR
# =========================================

class ContaPagar(models.Model):

    STATUS_CHOICES = [

        ('PENDENTE', 'Pendente'),
        ('PAGO', 'Pago'),
        ('VENCIDO', 'Vencido')

    ]

    # =========================================
    # ORIGEM
    # =========================================

    fornecedor = models.ForeignKey(

        Fornecedor,

        on_delete=models.PROTECT,

        related_name='contas_pagar',

        blank=True,

        null=True

    )

    profissional = models.ForeignKey(

        PerfilUsuario,

        on_delete=models.PROTECT,

        related_name='contas_pagar',

        blank=True,

        null=True

    )

    compra = models.ForeignKey(

        Compra,

        on_delete=models.SET_NULL,

        blank=True,

        null=True,

        related_name='contas_pagar'

    )

    # =========================================
    # CONTA A RECEBER QUE GEROU A COMISSÃO
    # =========================================

    conta_receber = models.OneToOneField(

        'ContaReceber',

        on_delete=models.SET_NULL,

        blank=True,

        null=True,

        related_name='comissao'

    )

    # =========================================
    # DADOS DA CONTA
    # =========================================

    descricao = models.CharField(

        max_length=255

    )

    valor = models.DecimalField(

        max_digits=12,

        decimal_places=2

    )

    vencimento = models.DateField()

    data_pagamento = models.DateField(

        blank=True,

        null=True

    )

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default='PENDENTE'

    )

    observacao = models.TextField(

        blank=True,

        null=True

    )

    criado_em = models.DateTimeField(

        auto_now_add=True

    )

    atualizado_em = models.DateTimeField(

        auto_now=True

    )

    class Meta:

        ordering = [

            'vencimento'

        ]

        verbose_name = 'Conta a Pagar'

        verbose_name_plural = 'Contas a Pagar'

    def __str__(self):

        if self.profissional:

            destino = self.profissional.usuario.get_full_name()

            if not destino:

                destino = self.profissional.usuario.username

        elif self.fornecedor:

            destino = self.fornecedor.nome

        else:

            destino = "Sem destino"

        return f"{destino} - {self.descricao} - R$ {self.valor}"

    @property
    def esta_vencida(self):

        from datetime import date

        return (

            self.status != 'PAGO'

            and

            self.vencimento < date.today()

        )

    @property
    def origem(self):

        if self.profissional:

            return "COMISSÃO"

        if self.fornecedor:

            return "FORNECEDOR"

        return "-"
        
# =========================================
# CONTAS A RECEBER
# =========================================

class ContaReceber(models.Model):

    STATUS_CHOICES = [

        ('PENDENTE', 'Pendente'),
        ('RECEBIDO', 'Recebido'),
        ('VENCIDO', 'Vencido'),
        ('CANCELADO', 'Cancelado'),

    ]

    # =========================================
    # RELACIONAMENTOS
    # =========================================

    paciente = models.ForeignKey(

        Paciente,

        on_delete=models.PROTECT,

        related_name='contas_receber'

    )

    orcamento = models.ForeignKey(

        Orcamento,

        on_delete=models.SET_NULL,

        blank=True,

        null=True,

        related_name='contas_receber'

    )

    # =========================================
    # DADOS DA CONTA
    # =========================================

    descricao = models.CharField(

        max_length=255

    )

    valor = models.DecimalField(

        max_digits=12,

        decimal_places=2

    )

    # =========================================
    # PARCELAMENTO
    # =========================================

    parcela = models.PositiveIntegerField(

        default=1

    )

    total_parcelas = models.PositiveIntegerField(

        default=1

    )

    # =========================================
    # DATAS
    # =========================================

    vencimento = models.DateField()

    data_recebimento = models.DateField(

        blank=True,

        null=True

    )

    # =========================================
    # STATUS
    # =========================================

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default='PENDENTE'

    )

    observacao = models.TextField(

        blank=True,

        null=True

    )

    # =========================================
    # CONTROLE
    # =========================================

    criado_em = models.DateTimeField(

        auto_now_add=True

    )

    atualizado_em = models.DateTimeField(

        auto_now=True

    )

    class Meta:

        ordering = ['vencimento']

        verbose_name = 'Conta a Receber'

        verbose_name_plural = 'Contas a Receber'

    @property
    def forma_pagamento(self):

        if self.orcamento:

            return self.orcamento.get_forma_pagamento_display()

        return "-"

    @property
    def numero_parcela(self):

        return f"{self.parcela}/{self.total_parcelas}"

    @property
    def tratamento(self):

        if self.orcamento:

            return self.orcamento.tratamento

        return None

    @property
    def dentista(self):

        tratamento = self.tratamento

        if tratamento:

            return tratamento.dentista

        return None

    @property
    def possui_comissao(self):

        return hasattr(self, "comissao")

    def __str__(self):

        return (

            f'{self.paciente.nome} - '

            f'Parcela {self.parcela}/{self.total_parcelas} - '

            f'R$ {self.valor}'

        )
        
# =========================================
# CAIXA
# =========================================

class Caixa(models.Model):

    TIPO_CHOICES = [

        ('ENTRADA', 'Entrada'),

        ('SAIDA', 'Saída')

    ]

    data = models.DateField()

    descricao = models.CharField(
        max_length=255
    )

    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES
    )

    valor = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    conta_pagar = models.ForeignKey(

        'ContaPagar',

        on_delete=models.SET_NULL,

        null=True,

        blank=True

    )

    conta_receber = models.ForeignKey(

        'ContaReceber',

        on_delete=models.SET_NULL,

        null=True,

        blank=True

    )

    # =========================================
    # USUÁRIO RESPONSÁVEL PELA MOVIMENTAÇÃO
    # =========================================

    usuario = models.ForeignKey(

        User,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name='movimentacoes_caixa'

    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = [

            '-data',
            '-id'

        ]

        verbose_name = 'Caixa'

        verbose_name_plural = 'Caixa'

    def __str__(self):

        return (

            f'{self.data} - '

            f'{self.descricao}'

        )

# =========================================
# CAIXA DIÁRIO
# =========================================

class CaixaDiario(models.Model):

    STATUS_CHOICES = [

        ("ABERTO", "Aberto"),

        ("FECHADO", "Fechado"),

    ]

    data = models.DateField()

    usuario = models.ForeignKey(

        User,

        on_delete=models.PROTECT,

        related_name="caixas_diarios",

    )

    saldo_inicial = models.DecimalField(

        max_digits=12,

        decimal_places=2,

        default=0

    )

    saldo_final = models.DecimalField(

        max_digits=12,

        decimal_places=2,

        default=0

    )

    data_abertura = models.DateTimeField(

        auto_now_add=True

    )

    data_fechamento = models.DateTimeField(

        null=True,

        blank=True

    )

    status = models.CharField(

        max_length=10,

        choices=STATUS_CHOICES,

        default="ABERTO"

    )

    observacoes = models.TextField(

        blank=True

    )

    class Meta:

        ordering = [

            "-data",

            "-id"

        ]

        verbose_name = "Caixa Diário"

        verbose_name_plural = "Caixas Diários"

    def __str__(self):

        return f"{self.data} - {self.get_status_display()}"

# =========================================
# FECHAMENTO MENSAL
# =========================================

class FechamentoMensal(models.Model):

    STATUS_CHOICES = [
        ("ABERTO", "Aberto"),
        ("FECHADO", "Fechado"),
    ]

    # =========================================
    # COMPETÊNCIA
    # =========================================

    ano = models.PositiveIntegerField(
        verbose_name="Ano"
    )

    mes = models.PositiveIntegerField(
        verbose_name="Mês"
    )

    # =========================================
    # RESUMO DO CAIXA
    # =========================================

    saldo_inicial = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    total_entradas = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    total_saidas = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    saldo_final = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    # =========================================
    # DRE
    # =========================================

    receita_bruta = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    total_comissoes = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    total_despesas = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    # =========================================
    # RESULTADO APÓS CUSTOS
    # =========================================

    resultado_apos_custos = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    # =========================================
    # RESULTADO OPERACIONAL
    # =========================================

    resultado_operacional = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    margem_operacional = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=Decimal("0.00")
    )

    # =========================================
    # INDICADORES OPERACIONAIS
    # =========================================

    procedimentos_realizados = models.PositiveIntegerField(
        default=0
    )

    pacientes_atendidos = models.PositiveIntegerField(
        default=0
    )

    ticket_medio = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    # =========================================
    # STATUS
    # =========================================

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="ABERTO"
    )

    # =========================================
    # RESPONSÁVEL PELO FECHAMENTO
    # =========================================

    usuario_fechamento = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="fechamentos_mensais"
    )

    data_fechamento = models.DateTimeField(
        null=True,
        blank=True
    )

    # =========================================
    # OBSERVAÇÕES
    # =========================================

    observacoes = models.TextField(
        blank=True
    )

    # =========================================
    # CONTROLE DE DATA
    # =========================================

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    # =========================================
    # META
    # =========================================

    class Meta:

        ordering = [
            "-ano",
            "-mes",
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "ano",
                    "mes",
                ],
                name="unique_fechamento_mensal"
            )

        ]

        indexes = [

            models.Index(
                fields=[
                    "ano",
                    "mes",
                ],
                name="idx_fechamento_ano_mes"
            ),

            models.Index(
                fields=[
                    "status",
                ],
                name="idx_fechamento_status"
            ),

        ]

    # =========================================
    # REPRESENTAÇÃO
    # =========================================

    def __str__(self):

        return (
            f"Fechamento "
            f"{self.mes:02d}/{self.ano}"
        )
        
# =========================================
# LIVRO CAIXA
# =========================================

class LivroCaixa(models.Model):

    TIPO_CHOICES = [

        ('ENTRADA', 'Entrada'),
        ('SAIDA', 'Saída'),

    ]

    ORIGEM_CHOICES = [

        ('CONTA_RECEBER', 'Conta a Receber'),
        ('CONTA_PAGAR', 'Conta a Pagar'),
        ('COMPRA', 'Compra'),
        ('COMISSAO', 'Comissão'),
        ('AJUSTE', 'Ajuste'),
        ('MANUAL', 'Manual'),

    ]

    # =========================================
    # DADOS DO LANÇAMENTO
    # =========================================

    data = models.DateField()

    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES
    )

    origem = models.CharField(
        max_length=30,
        choices=ORIGEM_CHOICES
    )

    descricao = models.CharField(
        max_length=255
    )

    entrada = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    saida = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    saldo = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    # =========================================
    # RELACIONAMENTOS
    # =========================================

    paciente = models.ForeignKey(

        Paciente,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="livro_caixa"

    )

    fornecedor = models.ForeignKey(

        Fornecedor,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="livro_caixa"

    )

    profissional = models.ForeignKey(

        PerfilUsuario,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="livro_caixa"

    )

    compra = models.ForeignKey(

        Compra,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="livro_caixa"

    )

    conta_receber = models.ForeignKey(

        'ContaReceber',

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="lancamentos_livro_caixa"

    )

    conta_pagar = models.ForeignKey(

        'ContaPagar',

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="lancamentos_livro_caixa"

    )

    # =========================================
    # OBSERVAÇÕES
    # =========================================

    observacao = models.TextField(

        blank=True,

        null=True

    )

    criado_em = models.DateTimeField(

        auto_now_add=True

    )

    # =========================================
    # CONFIGURAÇÕES
    # =========================================

    class Meta:

        ordering = [

            "-data",
            "-id"

        ]

        verbose_name = "Livro Caixa"

        verbose_name_plural = "Livro Caixa"

    def __str__(self):

        return (
            f"{self.data} - "
            f"{self.descricao}"
        )
    
# =========================================
# AUDITORIA
# =========================================

class Auditoria(models.Model):

    # =========================================
    # NÍVEL
    # =========================================

    NIVEL_CHOICES = (

        ("info", "Informação"),

        ("atencao", "Atenção"),

        ("importante", "Importante"),

        ("critico", "Crítico"),

    )

    # =========================================
    # AÇÃO
    # =========================================

    ACAO_CHOICES = (

        ("login", "Login"),

        ("logout", "Logout"),

        ("cadastro", "Cadastro"),

        ("edicao", "Edição"),

        ("exclusao", "Exclusão"),

        ("cancelamento", "Cancelamento"),

        ("aprovacao", "Aprovação"),

        ("recebimento", "Recebimento"),

        ("pagamento", "Pagamento"),

        ("impressao", "Impressão"),

        ("pdf", "PDF"),

        ("excel", "Excel"),

        ("backup", "Backup"),

        ("restauracao", "Restauração"),

        ("outro", "Outro"),

    )

    # =========================================
    # USUÁRIO
    # =========================================

    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="auditorias"
    )

    # =========================================
    # MÓDULO
    # =========================================

    modulo = models.CharField(
        max_length=50
    )

    # =========================================
    # AÇÃO
    # =========================================

    acao = models.CharField(
        max_length=20,
        choices=ACAO_CHOICES
    )

    # =========================================
    # NÍVEL
    # =========================================

    nivel = models.CharField(
        max_length=15,
        choices=NIVEL_CHOICES,
        default="info"
    )

    # =========================================
    # DESCRIÇÃO
    # =========================================

    descricao = models.TextField()

    # =========================================
    # OBJETO AFETADO
    # =========================================

    objeto_id = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    # =========================================
    # IP
    # =========================================

    ip = models.GenericIPAddressField(
        null=True,
        blank=True
    )

    # =========================================
    # DATA/HORA
    # =========================================

    data_hora = models.DateTimeField(
        auto_now_add=True
    )

    # =========================================
    # ORDENAÇÃO
    # =========================================

    class Meta:

        ordering = ["-data_hora"]

        verbose_name = "Auditoria"

        verbose_name_plural = "Auditorias"

    # =========================================
    # STRING
    # =========================================

    def __str__(self):

        usuario = (
            self.usuario.get_full_name()
            if self.usuario
            else "Sistema"
        )

        return (
            f"{self.data_hora:%d/%m/%Y %H:%M} - "
            f"{usuario} - "
            f"{self.modulo}"
        )
    

# =========================================
# PERMISSÕES
# =========================================

class Permissao(models.Model):

    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        related_name="permissoes"
    )

    modulo = models.ForeignKey(
        Modulo,
        on_delete=models.CASCADE,
        related_name="permissoes"
    )

    # =========================================
    # PERMISSÕES BÁSICAS
    # =========================================

    visualizar = models.BooleanField(
        default=False,
        verbose_name="Visualizar"
    )

    inserir = models.BooleanField(
        default=False,
        verbose_name="Inserir"
    )

    editar = models.BooleanField(
        default=False,
        verbose_name="Editar"
    )

    excluir = models.BooleanField(
        default=False,
        verbose_name="Excluir"
    )

    exportar = models.BooleanField(
        default=False,
        verbose_name="Exportar"
    )

    # =========================================
    # PERMISSÃO ESPECIAL
    # =========================================

    aprovar = models.BooleanField(
        default=False,
        verbose_name="Aprovar"
    )

    class Meta:
        unique_together = ("perfil", "modulo")
        ordering = ["perfil", "modulo"]
        verbose_name = "Permissão"
        verbose_name_plural = "Permissões"

    def __str__(self):
        return f"{self.perfil.nome} - {self.modulo.nome}"

# =========================================
# META DA CLÍNICA
# =========================================

class MetaClinica(models.Model):

    ano = models.PositiveIntegerField(
        "Ano"
    )

    mes = models.PositiveIntegerField(
        "Mês"
    )

    valor = models.DecimalField(
        "Meta",
        max_digits=12,
        decimal_places=2,
        default=0
    )

    observacao = models.TextField(
        "Observação",
        blank=True
    )

    ativo = models.BooleanField(
        default=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        verbose_name = "Meta da Clínica"
        verbose_name_plural = "Metas da Clínica"

        ordering = ["-ano", "-mes"]

        unique_together = (
            ("ano", "mes"),
        )

    def __str__(self):

        return f"{self.mes:02}/{self.ano} - R$ {self.valor}"


# =========================================
# META DO DENTISTA
# =========================================

class MetaDentista(models.Model):

    dentista = models.ForeignKey(
        PerfilUsuario,
        on_delete=models.CASCADE,
        limit_choices_to={
            "tipo_usuario": PerfilUsuario.DENTISTA,
            "ativo": True,
        },
        verbose_name="Dentista"
    )

    ano = models.PositiveIntegerField(
        "Ano"
    )

    mes = models.PositiveIntegerField(
        "Mês"
    )

    meta_financeira = models.DecimalField(
        "Meta Financeira",
        max_digits=12,
        decimal_places=2,
        default=0
    )

    meta_procedimentos = models.PositiveIntegerField(
        "Meta de Procedimentos",
        default=0
    )

    meta_pacientes = models.PositiveIntegerField(
        "Meta de Novos Pacientes",
        default=0
    )

    observacao = models.TextField(
        "Observação",
        blank=True
    )

    ativo = models.BooleanField(
        default=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        verbose_name = "Meta do Dentista"
        verbose_name_plural = "Metas dos Dentistas"

        ordering = ["-ano", "-mes", "dentista"]

        unique_together = (
            ("dentista", "ano", "mes"),
        )

    def __str__(self):

        return (
            f"{self.dentista} - "
            f"{self.mes:02}/{self.ano}"
        )

# =========================================
# LEADS (CRM / MARKETING)
# =========================================

class Lead(models.Model):

    ORIGEM_CHOICES = [

        ("GOOGLE", "Google Ads"),
        ("INSTAGRAM", "Instagram"),
        ("FACEBOOK", "Facebook"),
        ("WHATSAPP", "WhatsApp"),
        ("SITE", "Site"),
        ("INDICACAO", "Indicação"),
        ("OUTRO", "Outro"),

    ]

    STATUS_CHOICES = [

        ("NOVO", "Novo"),
        ("CONTATADO", "Contatado"),
        ("AGENDADO", "Agendado"),
        ("CONVERTIDO", "Convertido"),
        ("PERDIDO", "Perdido"),

    ]

    nome = models.CharField(
        max_length=150
    )

    telefone = models.CharField(
        max_length=20,
        blank=True
    )

    whatsapp = models.CharField(
        max_length=20,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    origem = models.CharField(
        max_length=20,
        choices=ORIGEM_CHOICES,
        default="OUTRO"
    )

    # =========================================
    # CAMPANHA DE MARKETING
    # =========================================

    campanha = models.ForeignKey(
        "CampanhaMarketing",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="leads",
        verbose_name="Campanha",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="NOVO"
    )

    observacoes = models.TextField(
        blank=True
    )

    responsavel = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="leads"
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True
    )

    ultimo_contato = models.DateTimeField(
        null=True,
        blank=True
    )

    proximo_contato = models.DateTimeField(
        null=True,
        blank=True
    )

    ativo = models.BooleanField(
        default=True
    )

    class Meta:

        ordering = ["-data_cadastro"]

        verbose_name = "Lead"

        verbose_name_plural = "Leads"

    def __str__(self):

        return self.nome

# =========================================
# HISTÓRICO DO LEAD
# =========================================

class HistoricoLead(models.Model):

    lead = models.ForeignKey(

        Lead,

        on_delete=models.CASCADE,

        related_name="historicos"

    )

    usuario = models.ForeignKey(

        User,

        on_delete=models.SET_NULL,

        null=True,

        blank=True

    )

    descricao = models.TextField(

        "Descrição"

    )

    data = models.DateTimeField(

        auto_now_add=True

    )

    class Meta:

        ordering = ["-data"]

        verbose_name = "Histórico do Lead"

        verbose_name_plural = "Históricos do Lead"

    def __str__(self):

        return f"{self.lead.nome} - {self.data:%d/%m/%Y %H:%M}"

# =========================================
# CAMPANHAS DE MARKETING
# =========================================

class CampanhaMarketing(models.Model):

    # =========================================
    # CANAIS
    # =========================================

    CANAL_CHOICES = [

        ("GOOGLE", "Google Ads"),
        ("INSTAGRAM", "Instagram"),
        ("FACEBOOK", "Facebook"),
        ("WHATSAPP", "WhatsApp"),
        ("SITE", "Site"),
        ("EMAIL", "E-mail Marketing"),
        ("OUTRO", "Outro"),

    ]

    # =========================================
    # STATUS
    # =========================================

    STATUS_CHOICES = [

        ("ATIVA", "Ativa"),
        ("PAUSADA", "Pausada"),
        ("FINALIZADA", "Finalizada"),

    ]

    # =========================================
    # DADOS DA CAMPANHA
    # =========================================

    nome = models.CharField(
        max_length=150
    )

    canal = models.CharField(
        max_length=20,
        choices=CANAL_CHOICES,
        default="GOOGLE"
    )

    descricao = models.TextField(
        blank=True
    )

    # =========================================
    # IMAGEM DA CAMPANHA
    # =========================================

    imagem = models.ImageField(
        upload_to="marketing/campanhas/",
        null=True,
        blank=True,
        verbose_name="Imagem da campanha",
    )
    # =========================================
    # PERÍODO
    # =========================================

    data_inicio = models.DateField()

    data_fim = models.DateField(
        null=True,
        blank=True
    )

    # =========================================
    # INVESTIMENTO
    # =========================================

    investimento = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    # =========================================
    # CONTROLE
    # =========================================

    ativa = models.BooleanField(
        default=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ATIVA"
    )

    # =========================================
    # USUÁRIO RESPONSÁVEL
    # =========================================

    criado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="campanhas_marketing"
    )

    # =========================================
    # DATA DE CRIAÇÃO
    # =========================================

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    # =========================================
    # META
    # =========================================

    class Meta:

        ordering = [
            "-data_inicio"
        ]

        verbose_name = "Campanha"

        verbose_name_plural = "Campanhas"

    # =========================================
    # STRING
    # =========================================

    def __str__(self):

        return self.nome

#=================================================    

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Lead)
def criar_historico_lead(sender, instance, created, **kwargs):

    if created:

        HistoricoLead.objects.create(

            lead=instance,

            usuario=instance.responsavel,

            descricao="Lead cadastrado no sistema."

        )


# =========================================
# VISUALIZAÇÕES DAS CAMPANHAS
# =========================================

class VisualizacaoCampanha(models.Model):

    campanha = models.ForeignKey(
        CampanhaMarketing,
        on_delete=models.CASCADE,
        related_name="visualizacoes",
        verbose_name="Campanha",
    )

    # Identifica a sessão do visitante
    sessao = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="Sessão",
    )

    # Quantas vezes essa mesma sessão acessou
    quantidade = models.PositiveIntegerField(
        default=1,
        verbose_name="Quantidade de acessos",
    )

    primeiro_acesso = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Primeiro acesso",
    )

    ultimo_acesso = models.DateTimeField(
        auto_now=True,
        verbose_name="Último acesso",
    )

    class Meta:

        verbose_name = "Visualização da Campanha"

        verbose_name_plural = "Visualizações das Campanhas"

        constraints = [

            models.UniqueConstraint(
                fields=["campanha", "sessao"],
                name="unique_visualizacao_campanha_sessao",
            )

        ]

    def __str__(self):

        return (
            f"{self.campanha.nome} - "
            f"{self.quantidade} acesso(s)"
        )
    


