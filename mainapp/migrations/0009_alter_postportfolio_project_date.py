# Generated by Django 4.0.5 on 2022-07-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_postportfolio_project_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postportfolio',
            name='project_date',
            field=models.DateTimeField(verbose_name='Fecha realización proyecto'),
        ),
    ]
