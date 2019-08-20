from django.db import models


class Screen(models.Model):
    inches = models.CharField(max_length=10)


class Ram(models.Model):
    length = models.CharField(max_length=10)


class Cpu(models.Model):
    name = models.CharField(max_length=25)


class Brand(models.Model):
    name = models.CharField(max_length=25)


class Price(models.Model):
    interval = models.CharField(max_length=25)


class Storage(models.Model):
    type = models.CharField(max_length=25)


class Link(models.Model):
    url = models.CharField(max_length=255)


class Notebook(models.Model):
    title = models.CharField(max_length=35)
    description = models.CharField(max_length=100)
    features = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    site = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    banner = models.CharField(max_length=500)

    def __str__(self):
        return self.title
