from django.db import models

# Create your models here.


class Wedstrijd(models.Model):
    wedstrijd_id = models.AutoField(primary_key=True, verbose_name="Id")
    tegenstander = models.CharField(
        max_length=200, verbose_name="Tegenstander")
    datum_wedstrijd = models.DateField(verbose_name="Datum")
    seizoen_wedstrijd = models.CharField( max_length=200, verbose_name="Seizoen", default='21/22')
    minuten_gespeeld = models.IntegerField(
        blank=False, null=False, default=90, verbose_name="Minuten gespeeld")
    soort_wedstrijd = models.CharField(
        max_length=300, choices=(('Competitie', 'Competitie'), ('Beker', 'Beker'), ('Oefen', 'Oefen')), default='', verbose_name="Soort wedstrijd")
    thuis_wedstrijd = models.BooleanField(verbose_name="Thuis wedstrijd?")


class Goal(models.Model):
    goal_id = models.AutoField(primary_key=True)
    Wedstrijd_id = models.IntegerField(blank=False, null=False)


class Assist(models.Model):
    assist_id = models.AutoField(primary_key=True)
    Wedstrijd_id = models.IntegerField(blank=False, null=False)
