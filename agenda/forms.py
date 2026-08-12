from django import forms

from .models import Agendamento


class AgendamentoForm(forms.ModelForm):

    class Meta:

        model = Agendamento

        fields = [

            'paciente',
            'profissional',
            'procedimento',
            'data',
            'hora_inicio',
            'duracao',
            'status',
            'observacoes'

        ]

        widgets = {

            'data': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'hora_inicio': forms.TimeInput(
                attrs={
                    'type': 'time'
                }
            ),

            'observacoes': forms.Textarea(
                attrs={
                    'rows': 4
                }
            )

        }