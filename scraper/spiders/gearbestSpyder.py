import scrapy
from scraper.items import NotebookItem, LinkItem
from selenium import webdriver
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import time
from core.models import Link


class NoteSpyder(scrapy.Spider):

    name = "note spyder"
    links = Link.objects.all()
    urls = [l.url for l in links]
    start_urls = urls

    def parse(self, response):       
        # print(response.body)
        title = response.css('h1.goodsIntro_title ::text').get()
        description = response.css('div.goodsIntro_summary ::text').get()
        price = response.css('span.goodsIntro_price ::text').get()
        features = response.css("div.product_pz_info b ::text").getall()
        banner = response.css(
            "div.goodsIntro_largeImgWrap img::attr('src')").get()

        print("banner", banner)
        print(title)
        print(description)
        print(price)
        features = filter(lambda x: x[0] == "●", features)
        features_str = ""
        for f in features:
            features_str += f + " "

        item = NotebookItem()
        item['title'] = title.lstrip().rstrip()
        item['description'] = description
        item['features'] = features_str
        item['price'] = float(price[1::])
        item['site'] = "gearbest"
        item['url'] = response.url
        item['banner'] = banner       
        yield item


class LinkSpyder(scrapy.Spider):
    name = "link spyder"
    start_urls = ["https://www.gearbest.com/laptops-c_11964/?page_size=120"]

    def parse(self, response):
        links = response.css("a.gbGoodsItem_title   ::attr('href')").getall()
        for link in links:
            item = LinkItem()
            item["url"] = link
            yield item

        next_page = response.css("a.pageNext::attr('href')").get()
        print("proxima  ", next_page)
        # verifica se chegou ao fim das paginas do site
        if next_page != "javascript:;":
            yield scrapy.Request(next_page, callback=self.parse)
