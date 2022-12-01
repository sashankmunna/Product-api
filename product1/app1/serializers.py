from rest_framework import serializers
from .models import ProductMainModel,ProductColorModel,ProductImageModel

class Productserializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=ProductMainModel
		fields="__all__"

class ProductColorserializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=ProductColorModel
		fields=('Product','Color')

class ProductImageserializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=ProductImageModel
		fields="__all__"

