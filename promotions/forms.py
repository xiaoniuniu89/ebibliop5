from django import forms

class PromoForm(forms.Form):
    code = forms.CharField()
