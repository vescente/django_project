from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Prints a greeting message'

    def handle(self, *args, **options):
        print("Hello, welcome to the Django management command!")