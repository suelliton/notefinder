from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from django.core.management import BaseCommand
from scraper.spiders.gearbestSpyder import LinkSpyder


class Command(BaseCommand):
    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        process.crawl(LinkSpyder)
        process.start()
