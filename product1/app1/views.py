from django.shortcuts import render
from rest_framework import viewsets
from .models import ProductMainModel,ProductColorModel,ProductImageModel
from .serializers import Productserializers,ProductColorserializers,ProductImageserializers

# Create your views here.
class ProductViewSets(viewsets.ModelViewSet):
	queryset=ProductMainModel.objects.all()
	serializer_class=Productserializers

class ProductColorViewSets(viewsets.ModelViewSet):
	queryset=ProductColorModel.objects.all()
	serializer_class=ProductColorserializers

class ProductImageViewSets(viewsets.ModelViewSet):
	queryset=ProductImageModel.objects.all()
	serializer_class=ProductImageserializers

def image_view(request):
	return render(request,'app1/home.html')
	

