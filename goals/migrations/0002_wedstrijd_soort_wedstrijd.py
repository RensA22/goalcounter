# Generated by Django 3.2.8 on 2021-10-28 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wedstrijd',
            name='soort_wedstrijd',
            field=models.CharField(choices=[(0, 'Competitie'), (1, 'Beker'), (2, 'Oefen')], default=0, max_length=300),
        ),
    ]