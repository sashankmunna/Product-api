from django.db import models

# Create your models here.
class ProductMainModel(models.Model):
	size_Choices=((1,'10'),(2,'20'),(3,'30'))
	quality_choices=(('H','High'),('L','Low'),('M','Medium'))
	Title=models.CharField(max_length=30)
	Description=models.TextField(max_length=100)
	Price=models.IntegerField()
	Size=models.IntegerField(choices=size_Choices)
	Quality=models.CharField(max_length=10, choices=quality_choices)


class ProductColorModel(models.Model):
	color_choice=(('R','Red'),('B','Blue'),('G','Green'),('Y','Yellow'))
	Product=models.ForeignKey("ProductMainModel", on_delete=models.CASCADE)
	Color=models.CharField(max_length=10, choices=color_choice)

class ProductImageModel(models.Model):
	Product=models.ForeignKey("ProductMainModel", on_delete=models.CASCADE)
	PImage=models.ImageField(null=True, upload_to="static/images")


