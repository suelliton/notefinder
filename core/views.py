from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SearchSerializer, NotebookSerializer
from rest_framework import generics
from .models import Notebook
from django.db.models import Q


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
            basic_filter.add(Q(description__contains=screen), Q.AND)

        if ram is not None:
            basic_filter.add(Q(description__contains=ram), Q.AND)

        if cpu is not None:
            basic_filter.add(Q(description__contains=cpu), Q.AND)

        if brand is not None:
            basic_filter.add(Q(description__contains=brand), Q.AND)

        if price is not None:
            basic_filter.add(Q(price__gte=str(price.split(
                " ")[0]), price__lte=str(price.split(" ")[2])), Q.AND)
            print(price.split(" ")[0])
            print(price.split(" ")[2])
        if storage is not None:
            basic_filter.add(Q(description__contains=storage), Q.AND)

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
                basic_filter.add(Q(description__contains=query), Q.OR)
        queryset = Notebook.objects.filter(basic_filter)
        return queryset


def home(request):
    return render(request, "core/home.html", {})
