import logging

from django.core.management.base import BaseCommand

logger = logging.getLogger('django_project_api')


class Command(BaseCommand):
    help = 'Custom Management Command'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        logger.info("Custom Management Command")
