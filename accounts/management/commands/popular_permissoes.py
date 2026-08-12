from django.core.management.base import BaseCommand

from accounts.models import Perfil, Modulo, Permissao


class Command(BaseCommand):
    help = "Cria e atualiza as permissões padrão dos perfis."

    def handle(self, *args, **options):

        criadas = 0
        atualizadas = 0

        perfis = Perfil.objects.filter(ativo=True).order_by("nome")
        modulos = Modulo.objects.filter(ativo=True).order_by("ordem")

        for perfil in perfis:

            for modulo in modulos:

                _, criado = Permissao.objects.update_or_create(

                    perfil=perfil,
                    modulo=modulo,

                    defaults={

                        "visualizar": False,
                        "inserir": False,
                        "editar": False,
                        "excluir": False,
                        "exportar": False,
                        "aprovar": False,

                    }

                )

                if criado:
                    criadas += 1
                else:
                    atualizadas += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"✔ {criadas} permissões criadas."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"✔ {atualizadas} permissões atualizadas."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"✔ Perfis processados: {perfis.count()}."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"✔ Módulos processados: {modulos.count()}."
            )
        )