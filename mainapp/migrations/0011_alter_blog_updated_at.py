# Generated by Django 4.0.5 on 2022-07-04 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='updated_at',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha actualización'),
        ),
    ]
