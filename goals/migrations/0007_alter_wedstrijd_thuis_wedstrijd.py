# Generated by Django 4.1.1 on 2022-09-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0006_wedstrijd_thuis_wedstrijd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wedstrijd',
            name='thuis_wedstrijd',
            field=models.BooleanField(verbose_name='Thuis wedstrijd?'),
        ),
    ]
