# Generated by Django 3.1.4 on 2021-06-19 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210619_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='option_1_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_2_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_3_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_4_count',
            field=models.IntegerField(default=0),
        ),
    ]