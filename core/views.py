from django.db.models import Q
from .models import Notebook, Screen, Ram, Cpu, Brand, Price, Storage
from rest_framework import generics
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (NotebookSerializer, ScreenSerializer, RamSerializer,
                          CpuSerializer, BrandSerializer, PriceSerializer, StorageSerializer)


class SearchViewSet(viewsets.ModelViewSet):
    serializer_class = NotebookSerializer

    def get_queryset(self):
        # queryset = Notebook.objects.all()
        # title = self.request.query_params.get('title', None)
        # print(title)
        # if title is not None:
        #    queryset = queryset.filter(title__contains=title)
        basic_filter = (Q())
        screen = self.request.query_params.get('screen', None)
        ram = self.request.query_params.get('ram', None)
        cpu = self.request.query_params.get('cpu', None)
        brand = self.request.query_params.get('brand', None)
        price = self.request.query_params.get('price', None)
        storage = self.request.query_params.get('storage', None)

        if screen is not None:
            #basic_filter.add(Q(title__contains=screen), Q.AND)
            basic_filter.add(Q(description__contains=screen), Q.AND)
            #basic_filter.add(Q(features__contains=screen), Q.AND)

        if ram is not None:
            #basic_filter.add(Q(title__contains=ram), Q.AND)
            basic_filter.add(Q(description__contains=ram), Q.AND)
            #basic_filter.add(Q(features__contains=ram), Q.AND)

        if cpu is not None:
            #basic_filter.add(Q(title__contains=cpu), Q.AND)
            basic_filter.add(Q(description__contains=cpu), Q.AND)
            #basic_filter.add(Q(features__contains=cpu), Q.AND)

        if brand is not None:
            basic_filter.add(Q(title__contains=brand), Q.AND)
            #basic_filter.add(Q(description__contains=brand), Q.OR)
            #basic_filter.add(Q(features__contains=brand), Q.OR)

        if price is not None:
            basic_filter.add(Q(price__gte=float(str(price.split(
                " ")[0])), price__lte=float(str(price.split(" ")[2]))), Q.AND)
            print(price.split(" ")[0])
            print(price.split(" ")[2])
        if storage is not None:
            basic_filter.add(Q(title__contains=storage), Q.AND)
            basic_filter.add(Q(description__contains=storage), Q.OR)
            #basic_filter.add(Q(features__contains=storage), Q.AND)

        queryset = Notebook.objects.filter(basic_filter)
        return queryset


class SearchFreeViewSet(viewsets.ModelViewSet):
    serializer_class = NotebookSerializer

    def get_queryset(self):
        basic_filter = (Q())
        query = self.request.query_params.get('query', None)
        if query is not None:
            list_query = query.split(" ")
            for query in list_query:
                basic_filter.add(Q(title__contains=query), Q.AND)
        queryset = Notebook.objects.filter(basic_filter)
        print(queryset)
        return queryset


class ScreenViewSet(viewsets.ModelViewSet):
    queryset = Screen.objects.all()
    serializer_class = ScreenSerializer


class RamViewSet(viewsets.ModelViewSet):
    queryset = Ram.objects.all()
    serializer_class = RamSerializer


class CpuViewSet(viewsets.ModelViewSet):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


def home(request):
    return render(request, "core/home.html", {})
