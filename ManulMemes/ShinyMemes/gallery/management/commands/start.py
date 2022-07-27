from django.core.management.base import BaseCommand
from Bot_app.utils import app
from aiogram import executor
from Bot_app.utils.handlers import dp
class Command(BaseCommand):
    def handle(self, *args, **options):
        executor.start_polling(dp, on_startup=app.on_startup)