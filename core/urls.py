from django.urls import path, include
from .views import (home, SearchViewSet, SearchFreeViewSet, ScreenViewSet,
                    RamViewSet, CpuViewSet, BrandViewSet, PriceViewSet, StorageViewSet)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'search', SearchViewSet, basename="search")
router.register(r'freesearch', SearchFreeViewSet, basename="freesearch")

router.register(r'screen', ScreenViewSet, basename="screen")
router.register(r'ram', RamViewSet, basename="ram")
router.register(r'cpu', CpuViewSet, basename="cpu")
router.register(r'brand', BrandViewSet, basename="brand")
router.register(r'price', PriceViewSet, basename="price")
router.register(r'storage', StorageViewSet, basename="storage")


urlpatterns = [
    path('', home, name="home"),
    path('', include(router.urls)),
]
