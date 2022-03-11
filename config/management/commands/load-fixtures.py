from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "user_fixture.json")
        call_command("loaddata", "member_fixture.json")
        call_command("loaddata", "dashboard_fixture.json")
        call_command("loaddata", "dashboard_column_fixture.json")
        call_command("loaddata", "todo_item_fixture.json")
