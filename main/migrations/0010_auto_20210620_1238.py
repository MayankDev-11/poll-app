# Generated by Django 3.1.4 on 2021-06-20 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210620_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(upload_to='photos/%Y/%M/%d'),
        ),
    ]
