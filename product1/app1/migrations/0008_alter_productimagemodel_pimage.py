# Generated by Django 4.1.2 on 2022-11-30 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_productimagemodel_pimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimagemodel',
            name='PImage',
            field=models.ImageField(null=True, upload_to='blog/%Y/%m/%d'),
        ),
    ]
