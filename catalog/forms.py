from django import forms
from django.core.validators import MinValueValidator


class AutoCostFilterForm(forms.Form):
    min_price = forms.IntegerField(label='Цена от', required=False, validators=[MinValueValidator(0)])
    max_price = forms.IntegerField(label='Цена до', required=False, validators=[MinValueValidator(0)])
