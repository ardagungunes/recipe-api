"""
Django command to wait for the database to be available.
"""
import time

from psycopg2 import OperationalError as 

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for database."""
    
    def handle(self, *args, **options):
        pass