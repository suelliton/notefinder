from django.urls import path, include
from .views import home, SearchViewSet, SearchFreeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'search', SearchViewSet, basename="search")
router.register(r'freesearch', SearchFreeViewSet, basename="freesearch")


urlpatterns = [
    path('', home, name="home"),
    path('', include(router.urls)),
]
