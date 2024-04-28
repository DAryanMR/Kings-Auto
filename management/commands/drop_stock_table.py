from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Drops the stock table'

    def handle(self, *args, **kwargs):
        # Use a raw SQL query to drop the stock table
        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS stock;")

        # Print success message to console
        self.stdout.write(self.style.SUCCESS(
            'Successfully dropped the stock table'))
