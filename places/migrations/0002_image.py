# Generated by Django 4.2.3 on 2023-08-10 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('imgs', models.ImageField(upload_to='media/', verbose_name='Картинка')),
            ],
        ),
    ]