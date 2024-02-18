from django import forms

class CheckVinForm(forms.Form):
    vin = forms.CharField(max_length=17, label='Введите VIN')

