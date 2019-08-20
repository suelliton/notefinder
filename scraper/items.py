# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from core.models import Notebook, Link


class NotebookItem(DjangoItem):
    django_model = Notebook


class LinkItem(DjangoItem):
    django_model = Link
