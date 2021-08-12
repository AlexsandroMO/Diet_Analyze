from django import forms
from .models import NutriCalc


class NutriCalcForm(forms.ModelForm):
    class Meta:
        model = NutriCalc
        fields = ('food_name','qt_g','ptn','gli','lip','ca','p','fe','vit_a','tia','ribo','nia','vit_c','fiber')