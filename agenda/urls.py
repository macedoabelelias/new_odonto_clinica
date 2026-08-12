from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.agenda_view,
        name='agenda'
    ),

     path(
        'novo/',
        views.novo_agendamento,
        name='novo_agendamento'
    ),

    path(
        'novo/<int:paciente_id>/',
        views.novo_agendamento_paciente,
        name='novo_agendamento_paciente'
    ),

    path(
        'iniciar-atendimento/<int:agendamento_id>/',
        views.iniciar_atendimento,
        name='iniciar_atendimento'
    ),

    path(
        'editar/<int:id>/',
        views.editar_agendamento,
        name='editar_agendamento'
    ),

    path(
        'finalizar/<int:agendamento_id>/',
        views.finalizar_atendimento,
        name='finalizar_atendimento'
    ),

    path(
        'eventos/',
        views.eventos_agenda,
        name='eventos_agenda'
    ),

    path(
        'mover-agendamento/',
        views.mover_agendamento,
        name='mover_agendamento'
    ),

    path(
        'confirmar/<int:agendamento_id>/',
        views.confirmar_agendamento,
        name='confirmar_agendamento'
    ),

    path(
        'faltou/<int:agendamento_id>/',
        views.marcar_falta,
        name='marcar_falta'
    ),

    path(
        'cancelar/<int:agendamento_id>/',
        views.cancelar_agendamento,
        name='cancelar_agendamento'
    ),

    path(
        'alterar-status/',
        views.alterar_status_ajax,
        name='alterar_status_ajax'
    ),

    
]