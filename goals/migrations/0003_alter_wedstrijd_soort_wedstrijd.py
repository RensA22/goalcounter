# Generated by Django 3.2.8 on 2021-10-28 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_wedstrijd_soort_wedstrijd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wedstrijd',
            name='soort_wedstrijd',
            field=models.CharField(choices=[('Competitie', 'Competitie'), ('Beker', 'Beker'), ('Oefen', 'Oefen')], default='', max_length=300),
        ),
    ]