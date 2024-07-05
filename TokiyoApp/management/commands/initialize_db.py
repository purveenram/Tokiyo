from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Initialize the database'

    def handle(self, *args, **options):
        call_command('migrate')
        # Optionally load initial data
        # call_command('loaddata', 'initial_data.json')
