from django import forms
from .models import NutriCalc, Anamnesi


class NutriCalcForm(forms.ModelForm):
    class Meta:
        model = NutriCalc
        fields = ('food_name','qt_g','ptn','gli','lip','ca','p','fe','vit_a','tia','ribo','nia','vit_c','fiber')


class AnamnesiForm(forms.ModelForm):
    class Meta:
        model = Anamnesi
        fields = ('patient_name','cpf','age_date','gener','marital_st','sons','schooling','profession','cep','street','number',
        'district','city','state','cel','email','consult_motivation','leisure_habits','food_allergies','urinary_habits','bowel_habits',
        'pathologies_symptoms','stress','headache','frequent_infections','abdominal_pain','digestion','skin_nail_hair','sleep',
        'time_feel_hungry','essential_foods','candy_ingestion','ingestion_snacks_frying',)



