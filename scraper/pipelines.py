# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from core.models import Notebook, Link


class NotebookPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "note spyder":
            if not Notebook.objects.filter(title=item['title']):
                item.save()
        elif spider.name == "link spyder":
            if not Link.objects.filter(url=item['url']):
                item.save()
        return item
