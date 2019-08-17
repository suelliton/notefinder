from django.db import models


class Search(models.Model):
    screen = models.CharField(max_length=25)
    ram = models.CharField(max_length=25)
    cpu = models.CharField(max_length=25)
    brand = models.CharField(max_length=25)
    price = models.CharField(max_length=25)
    storage = models.CharField(max_length=25)


class Notebook(models.Model):
    title = models.CharField(max_length=35)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    site = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    banner = models.CharField(max_length=500)

    def __str__(self):
        return self.modelo + " " + self.marca
