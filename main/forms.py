from django import forms
from django.forms.fields import CharField
from django.forms.widgets import Select, Textarea, NumberInput


FLUCTUATYION_CHOICES = (
    (5, "Très elevé"),
    (4, "elevé"),
    (3, "moyenne"),
    (2, "faible"),
    (1, "quasi inexistante"),
)

Target_CHOICES = (
    ( 6, "B2B"),
    ( 12, "B2C"),
)

Public_CHOICES =(
    (1,"large"),
    (2,"ciblé")

)

class mainform(forms.Form):
    
    nom_entr = forms.CharField(
                              label="Nom entreprise", error_messages={'required': "veuillez saisir le nom de l'entreprise"})
    Activité = forms.CharField( label="Activité",
            widget=Textarea(attrs={'placeholder': 'ex: Vente en ligne de chaussure','rows':7,  "style":"width : 100%;"}) , error_messages={'required': "veuillez saisir votre activité"})

    CA = forms.FloatField(label="Chiffre d'affaire", error_messages={'required': "veuillez saisir votre CA"})
    M_inve = forms.FloatField(label="Montant Investissement financier", error_messages={'required': "veuillez saisir votre investissement financier"})

    M_dette = forms.FloatField(label="Montant des dettes", error_messages={'required': "veuillez saisir le montant de vos dettes"})

    fluctuation = forms.ChoiceField(label="Fluctuatuions du Chiffre d'affaire",
                                     choices=FLUCTUATYION_CHOICES, widget=Select, error_messages={'required': 'Veuillez choisir un moyen de paiement'})

    nom_site = forms.CharField(label="Nom site web")

    Systeme = forms.ChoiceField(
            choices=Target_CHOICES, widget=forms.RadioSelect,)                   

    Target = forms.ChoiceField(
            choices=Public_CHOICES, widget=forms.RadioSelect,)

    budget_pub = forms.FloatField(widget=forms.HiddenInput())