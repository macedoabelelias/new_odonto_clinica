from django import forms
from django.utils import timezone
from django.contrib.auth.models import User

from .models import (
    PerfilUsuario,
    Procedimento,
    Orcamento,
    ItemOrcamento,
    Convenio,
    Perfil,
    Receita,
    ModeloReceita,
    MetaDentista,
    Lead,
    CampanhaMarketing,
)




# =========================================
# FORM PROCEDIMENTO
# =========================================

class ProcedimentoForm(forms.ModelForm):

    class Meta:

        model = Procedimento

        fields = [

            'nome',
            'categoria',
            'tipo',
            'status',

            'icone',
            'arquivo_icone',

            'posicao_icone',

            'valor_particular',

            'tempo_estimado',
            'custo_clinico',

            'ativo',

        ]

        widgets = {

    'nome': forms.TextInput(

        attrs={

            'class': 'form-control shadow-sm'

        }

    ),

    'categoria': forms.Select(

        attrs={

            'class': 'form-select shadow-sm'

        }

    ),

    'tipo': forms.Select(

        attrs={

            'class': 'form-select shadow-sm'

        }

    ),

    'status': forms.Select(

        attrs={

            'class': 'form-select shadow-sm'

        }

    ),

    # ===== POSIÇÃO ÍCONE =====
    'posicao_icone': forms.Select(

        attrs={

            'class': 'form-select shadow-sm'

        }

    ),

    'icone': forms.TextInput(

        attrs={

            'class': 'form-control shadow-sm',

            'placeholder': 'Digite ou pesquise um ícone'

        }

    ),

    'valor_particular': forms.NumberInput(

        attrs={

            'class': 'form-control shadow-sm',

            'step': '0.01',

            'placeholder': 'Valor Particular'

        }

    ),

    'valor_convenio': forms.NumberInput(

        attrs={

            'class': 'form-control shadow-sm',

            'step': '0.01',

            'placeholder': 'Valor Convênio'

        }

    ),
    

    'tempo_estimado': forms.NumberInput(

        attrs={

            'class': 'form-control shadow-sm',

            'placeholder': 'Tempo em minutos'

        }

    ),

    'custo_clinico': forms.NumberInput(

        attrs={

            'class': 'form-control shadow-sm',

            'step': '0.01',

            'placeholder': 'Custo Clínico'

        }

    ),

    'ativo': forms.CheckboxInput(

        attrs={

            'class': 'form-check-input'

        }

    ),

    'ordem': forms.NumberInput(

        attrs={

            'class': 'form-control shadow-sm'

        }

    )

}


# =========================================
# ORÇAMENTO
# =========================================

class OrcamentoForm(forms.ModelForm):

    class Meta:

        model = Orcamento

        fields = [

            'desconto',
            'observacoes'

        ]

        widgets = {

            'desconto': forms.NumberInput(

                attrs={

                    'class': 'form-control',

                    'step': '0.01'

                }

            ),

            'observacoes': forms.Textarea(

                attrs={

                    'class': 'form-control',

                    'rows': 3

                }

            )

        }


# =========================================
# ITEM ORÇAMENTO
# =========================================

class ItemOrcamentoForm(forms.ModelForm):

    class Meta:

        model = ItemOrcamento

        fields = [

            'procedimento',
            'quantidade'

        ]

        widgets = {

            'procedimento': forms.Select(

                attrs={

                    'class': 'form-select rounded-3 shadow-sm'

                }

            ),

            'quantidade': forms.NumberInput(

                attrs={

                    'class': 'form-control rounded-3 shadow-sm',
                    'min': 1

                }

            )

        }
        
 # =========================================
# FORM CONVÊNIO
# =========================================

class ConvenioForm(forms.ModelForm):

    class Meta:

        model = Convenio

        fields = [

            'nome',
            'indice',
            'telefone',
            'observacoes',
            'ativo'

        ]

        widgets = {

            'nome': forms.TextInput(

                attrs={

                    'class': 'form-control shadow-sm'

                }

            ),

            'indice': forms.NumberInput(

                attrs={

                    'class': 'form-control shadow-sm',
                    'step': '0.01'

                }

            ),

            'telefone': forms.TextInput(

                attrs={

                    'class': 'form-control shadow-sm'

                }

            ),

            'observacoes': forms.Textarea(

                attrs={

                    'class': 'form-control shadow-sm',
                    'rows': 3

                }

            ),

            'ativo': forms.CheckboxInput(

                attrs={

                    'class': 'form-check-input'

                }

            )

        }  


# =========================================
# FORM PERFIL
# =========================================

from .models import Perfil


class PerfilForm(forms.ModelForm):

    class Meta:

        model = Perfil

        fields = [

            'nome',
            'descricao',
            'ativo',

        ]

        widgets = {

            'nome': forms.TextInput(

                attrs={

                    'class': 'form-control shadow-sm',

                    'placeholder': 'Nome do perfil'

                }

            ),

            'descricao': forms.Textarea(

                attrs={

                    'class': 'form-control shadow-sm',

                    'rows': 3,

                    'placeholder': 'Descrição do perfil'

                }

            ),

            'ativo': forms.CheckboxInput(

                attrs={

                    'class': 'form-check-input'

                }

            ),

        }  

# =========================================
# FORM META DOS DENTISTAS
# =========================================

from django.utils import timezone


class MetaDentistaForm(forms.ModelForm):

    MESES = (

        (1, "Janeiro"),
        (2, "Fevereiro"),
        (3, "Março"),
        (4, "Abril"),
        (5, "Maio"),
        (6, "Junho"),
        (7, "Julho"),
        (8, "Agosto"),
        (9, "Setembro"),
        (10, "Outubro"),
        (11, "Novembro"),
        (12, "Dezembro"),

    )

    class Meta:

        model = MetaDentista

        fields = [

            "dentista",
            "mes",
            "ano",
            "meta_financeira",
            "meta_procedimentos",
            "meta_pacientes",
            "observacao",

        ]

        widgets = {

            "mes": forms.NumberInput(
                attrs={
                    "class": "form-control shadow-sm",
                    "min": 1,
                    "max": 12,
                }
            ),

            "ano": forms.NumberInput(

                attrs={

                    "class": "form-control shadow-sm",

                }

            ),

            "meta_financeira": forms.NumberInput(

                attrs={

                    "class": "form-control shadow-sm",
                    "step": "0.01",

                }

            ),

            "meta_procedimentos": forms.NumberInput(

                attrs={

                    "class": "form-control shadow-sm",
                    "min": 0,

                }

            ),

            "meta_pacientes": forms.NumberInput(

                attrs={

                    "class": "form-control shadow-sm",
                    "min": 0,

                }

            ),

            "observacao": forms.Textarea(

                attrs={

                    "class": "form-control shadow-sm",
                    "rows": 3,

                }

            ),

        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # =========================================
        # DENTISTAS
        # =========================================

        queryset = PerfilUsuario.objects.filter(

            tipo_usuario=PerfilUsuario.DENTISTA,

            ativo=True,

        ).order_by(

            "usuario__first_name",

            "usuario__last_name",

        )

        self.fields["dentista"].queryset = queryset

        self.fields["dentista"].label_from_instance = (

            lambda obj: obj.usuario.get_full_name() or obj.usuario.username

        )

        self.fields["dentista"].widget.attrs.update({

            "class": "form-select shadow-sm",

        })

        # =========================================
        # MÊS
        # =========================================

        self.fields["mes"].widget = forms.Select(

            choices=[

                (1, "Janeiro"),
                (2, "Fevereiro"),
                (3, "Março"),
                (4, "Abril"),
                (5, "Maio"),
                (6, "Junho"),
                (7, "Julho"),
                (8, "Agosto"),
                (9, "Setembro"),
                (10, "Outubro"),
                (11, "Novembro"),
                (12, "Dezembro"),

            ],

            attrs={

                "class": "form-select shadow-sm",

            },

        )

        # =========================================
        # VALORES PADRÃO
        # =========================================

        hoje = timezone.now()

        self.fields["mes"].initial = hoje.month

        self.fields["ano"].initial = hoje.year

        if queryset.exists():

            self.fields["dentista"].initial = queryset.first()


# =========================================
# FORMULÁRIO DE LEADS
# =========================================

class LeadForm(forms.ModelForm):

    class Meta:

        model = Lead

        fields = [

            "nome",
            "telefone",
            "whatsapp",
            "email",
            "origem",
            "campanha",
            "status",
            "responsavel",
            "observacoes",
            "proximo_contato",
            "ativo",

        ]

        widgets = {

            "nome": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "telefone": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "whatsapp": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control"
            }),

            "origem": forms.Select(attrs={
                "class": "form-select"
            }),

            "campanha": forms.Select(attrs={
                "class": "form-select"
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),

            "responsavel": forms.Select(attrs={
                "class": "form-select"
            }),

            "proximo_contato": forms.DateTimeInput(attrs={
                "class": "form-control",
                "type": "datetime-local"
            }),

            "observacoes": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4
            }),

            "ativo": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),

        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # =========================================
        # RESPONSÁVEIS
        # =========================================

        queryset = User.objects.filter(
            perfil__tipo_usuario__in=[
                PerfilUsuario.ADMIN,
                PerfilUsuario.GESTOR,
                PerfilUsuario.MARKETING,
            ]
        )

        self.fields["responsavel"].queryset = queryset

        # =========================================
        # CAMPANHAS
        # =========================================

        self.fields["campanha"].queryset = (
            CampanhaMarketing.objects
            .filter(
                ativa=True
            )
            .order_by(
                "-data_inicio"
            )
        )

        self.fields["campanha"].required = False

# =========================================
# FORMULÁRIO PÚBLICO DE CAPTAÇÃO DE LEADS
# =========================================

class LeadCaptacaoForm(forms.ModelForm):

    class Meta:

        model = Lead

        fields = [
            "nome",
            "telefone",
            "whatsapp",
            "email",
        ]

        widgets = {

            "nome": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Digite seu nome",
                "autocomplete": "name",
            }),

            "telefone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "(00) 00000-0000",
                "autocomplete": "tel",
            }),

            "whatsapp": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "(00) 00000-0000",
                "autocomplete": "tel",
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "seu@email.com",
                "autocomplete": "email",
            }),

        }

    def clean(self):

        cleaned_data = super().clean()

        telefone = cleaned_data.get("telefone")
        whatsapp = cleaned_data.get("whatsapp")

        if not telefone and not whatsapp:

            raise forms.ValidationError(
                "Informe pelo menos um telefone ou WhatsApp para que possamos entrar em contato."
            )

        return cleaned_data


# =========================================
# CAPTAÇÃO PÚBLICA DE LEAD
# =========================================

def captacao_campanha(request, pk):

    campanha = get_object_or_404(
        CampanhaMarketing,
        pk=pk,
        ativa=True,
        status="ATIVA",
    )

    if request.method == "POST":

        form = LeadCaptacaoForm(
            request.POST
        )

        if form.is_valid():

            lead = form.save(
                commit=False
            )

            # =========================================
            # VINCULAR À CAMPANHA
            # =========================================

            lead.campanha = campanha

            # =========================================
            # STATUS INICIAL
            # =========================================

            lead.status = "NOVO"

            # =========================================
            # ORIGEM DA CAMPANHA
            # =========================================

            if campanha.canal in [
                "GOOGLE",
                "INSTAGRAM",
                "FACEBOOK",
                "WHATSAPP",
                "SITE",
            ]:

                lead.origem = campanha.canal

            else:

                lead.origem = "OUTRO"

            # =========================================
            # LEAD ATIVO
            # =========================================

            lead.ativo = True

            lead.save()

            # =========================================
            # HISTÓRICO
            # =========================================

            HistoricoLead.objects.create(

                lead=lead,

                descricao=(
                    f"Lead captado através da campanha "
                    f"'{campanha.nome}'."
                ),

            )

            return render(
                request,
                "accounts/marketing/campanha_sucesso.html",
                {
                    "campanha": campanha,
                },
            )

    else:

        form = LeadCaptacaoForm()

    return render(
        request,
        "accounts/marketing/campanha_publica.html",
        {
            "campanha": campanha,
            "form": form,
        },
    )

    

# =========================================
# FORMULÁRIO DE CAMPANHAS DE MARKETING
# =========================================

class CampanhaMarketingForm(forms.ModelForm):

    class Meta:

        model = CampanhaMarketing

        fields = [
            "nome",
            "canal",
            "descricao",
            "imagem",
            "data_inicio",
            "data_fim",
            "investimento",
            "ativa",
            "status",
        ]
        widgets = {

            "nome": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nome da campanha"
            }),

            "canal": forms.Select(attrs={
                "class": "form-select"
            }),

            "descricao": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Descrição da campanha"
            }),

            "imagem": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "accept": "image/*",
            }),

            # =========================================
            # IMAGEM DA CAMPANHA
            # =========================================

            "imagem": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "accept": "image/*"
            }),

            "data_inicio": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "data_fim": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "investimento": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01",
                "min": "0"
            }),

            "ativa": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),
        }