# Generated by Django 3.2.4 on 2021-06-18 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='photos/%Y/%M/%d')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('option_1', models.CharField(max_length=255)),
                ('option_2', models.CharField(max_length=255)),
                ('option_3', models.CharField(max_length=255)),
                ('option_4', models.CharField(max_length=255)),
                ('option_1_count', models.IntegerField()),
                ('option_2_count', models.IntegerField()),
                ('option_3_count', models.IntegerField()),
                ('option_4_count', models.IntegerField()),
            ],
        ),
    ]