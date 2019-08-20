from rest_framework import serializers
from .models import Notebook, Screen, Ram, Cpu, Brand, Price, Storage


class NotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = '__all__'


class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = '__all__'


class RamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ram
        fields = '__all__'


class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'
