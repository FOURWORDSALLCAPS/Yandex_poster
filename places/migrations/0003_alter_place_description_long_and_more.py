# Generated by Django 4.2.3 on 2023-08-14 11:40

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_place_description_long_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Длинное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
    ]