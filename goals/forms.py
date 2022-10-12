from django import forms
from.models import Wedstrijd, Goal, Assist


class DataForm(forms.Form):
    datum_wedstrijd = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date', 'class': 'form-control'}))
    seizoen = forms.ChoiceField(
        choices=(("21/22", '21/22'),
                 ('22/23', '22/23')),
        widget=forms.Select(attrs={'class': 'form-control'}))
    tegenstander = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    aantal_goals = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    aantal_assists = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    minuten_gespeeld = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    soort_wedstrijd = forms.ChoiceField(
        choices=(("Competitie", 'Competitie'),
                 ('Beker', 'Beker'), ('Oefen', 'Oefen')),
        widget=forms.Select(attrs={'class': 'form-control'}))
    thuis_wedstrijd = forms.BooleanField(required=False)
