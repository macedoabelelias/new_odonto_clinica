from django.contrib import admin

from .models import (
    Profissional,
    Agendamento
)


@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'especialidade',
        'ativo'
    )

    search_fields = (
        'nome',
        'especialidade'
    )


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):

    list_display = (
        'paciente',
        'profissional',
        'data',
        'hora_inicio',
        'status'
    )

    list_filter = (
        'status',
        'data',
        'profissional'
    )

    search_fields = (
        'paciente__nome',
    )