from random import choice as choices
from django.core.management import BaseCommand
from core.models import Screen, Ram, Cpu, Brand, Price, Storage
from .utils import screens, rams, brands


class Command(BaseCommand):

    def handle(self, *args, **options):
        """   
        for inches in screens:
            s = Screen(inches=inches)
            s.save()
        for ram in rams:
            s = Ram(length=ram)
            s.save()

        for cpu in cpus:
            s = Cpu(name=cpu)
            s.save()"""
        for brand in brands:
            s = Brand(name=brand)
            s.save()
        """
        for price in prices_front:
            s = Price(interval=prices_front)
            s.save()
        for storage in storages:
            s = Storage(type=storage)
            s.save()"""
