from django.core.management import BaseCommand
from core.models import Notebook
from random import choice as choices


class Command(BaseCommand):
    cpus = ["I7", "I5", "I3", "Pentium"]
    brands = ["Sony",  "Acer", "Xiomi", "Dell"]
    models = ["Mi Ruby", "EZBook x4", "EZBook x1", "AeroBook"]
    rams = [2, 4, 8, 16, 32, 64]
    prices = [1.000, 2.000, 3.000, 4.000, 5.000,
              6.000, 7.000, 8.000, 9.000, 10.000, 15.000]
    screens = [8, 10, 11, 13, 14, 15, 15, 17]
    banners = ["https://gloimg.gbtcdn.com/soa/gb/pdm-product-pic/Electronic/2019/04/20/goods_thumb_220-v2/20190420113527_95288.jpg",
               "https://gloimg.gbtcdn.com/soa/gb/pdm-product-pic/Electronic/2019/05/27/goods_thumb_220-v1/20190527135441_59259.jpg",
               "https://gloimg.gbtcdn.com/soa/gb/pdm-product-pic/Electronic/2019/05/10/goods_thumb_220-v2/20190510173420_85369.jpg",
               "https://gloimg.gbtcdn.com/soa/gb/pdm-product-pic/Electronic/2019/06/17/goods_thumb_220-v2/20190617111852_52305.jpg",
               "https://gloimg.gbtcdn.com/soa/gb/pdm-product-pic/Electronic/2019/04/24/goods_thumb_220-v1/20190424134558_84181.jpg",
               "https://gloimg.gbtcdn.com/soa/gb/pdm-product-pic/Electronic/2018/09/14/goods_thumb_220-v1/20180914134850_19656.jpg",
               "https://gloimg.gbtcdn.com/soa/gb/pdm-product-pic/Electronic/2019/05/13/goods_thumb_220-v1/20190513133504_52953.jpg",
               "https://gloimg.gbtcdn.com/soa/gb/pdm-product-pic/Electronic/2019/05/28/goods_thumb_220-v1/20190528183514_79595.jpg"
               ]
    titles = []
    descriptions = []
    for t in range(100):
        titles.append(choices(models)+" " + choices(brands)+" "+choices(cpus))
        descriptions.append(choices(cpus)+" "+choices(brands) +
                            " "+choices(models)+" "+str(choices(rams))+" "
                            + str(choices(screens)))

    def handle(self, *args, **options):
        print("Iniciando geração de dados")
        for i in range(100):

            notebook = Notebook(
                title=choices(self.titles),
                description=choices(self.descriptions),
                banner=choices(self.banners),
                price=choices(self.prices),
                site="Gearbest",
                url="https://www.google.com"
            )
            notebook.save()
        print("Geração de dados finalizada")
