# Generated by Django 5.2 on 2025-04-10 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_manufacturer_tag_cardetail_car_manufacturer_car_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='is_published',
            field=models.IntegerField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=0, verbose_name='Статус публикации'),
        ),
    ]
