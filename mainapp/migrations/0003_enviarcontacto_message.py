# Generated by Django 4.0.5 on 2022-06-27 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_enviarcontacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='enviarcontacto',
            name='message',
            field=models.TextField(default='Null'),
        ),
    ]
