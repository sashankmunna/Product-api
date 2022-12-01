from django.contrib import admin

# Register your models here.
from app1.models import ProductMainModel,ProductColorModel,ProductImageModel

class PMMAdmin(admin.ModelAdmin):
	list_display=['Title','Description','Price','Size','Quality']
admin.site.register(ProductMainModel, PMMAdmin)

class PCMAdmin(admin.ModelAdmin):
	list_display=['Product','Color']
admin.site.register(ProductColorModel,PCMAdmin)

class PIMAdmin(admin.ModelAdmin):
	list_display=['Product','PImage']
admin.site.register(ProductImageModel,PIMAdmin)