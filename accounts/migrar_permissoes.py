from accounts.models import Modulo, Permissao

MAPA = {
    1: 37,
    2: 38,
    3: 39,
    4: 40,
    5: 41,
    6: 42,
    7: 45,
    8: 46,
    9: 47,
    10: 48,
    11: 49,
    12: 50,
}

total = 0

for antigo_id, novo_id in MAPA.items():

    antigo = Modulo.objects.get(id=antigo_id)
    novo = Modulo.objects.get(id=novo_id)

    for perm in Permissao.objects.filter(modulo=antigo):

        nova_perm, created = Permissao.objects.get_or_create(
            perfil=perm.perfil,
            modulo=novo
        )

        nova_perm.visualizar = perm.visualizar
        nova_perm.inserir = perm.inserir
        nova_perm.editar = perm.editar
        nova_perm.excluir = perm.excluir
        nova_perm.exportar = perm.exportar

        nova_perm.save()

        total += 1

print(f"{total} permissões migradas com sucesso.")