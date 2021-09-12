from django import forms
from .models import Anamnesi, Anthropometric, NutriCalc





class AnamnesiForm(forms.ModelForm):
    class Meta:
        model = Anamnesi
        fields = ('patient_name','cpf','age_date','gener','marital_st','sons','schooling','profession','cep','street','number',
        'district','city','state','cel','email','consult_motivation','leisure_habits','food_allergies','urinary_habits','bowel_habits',
        'pathologies_symptoms','stress','headache','frequent_infections','abdominal_pain','digestion','skin_nail_hair','sleep',
        'time_feel_hungry','essential_foods','candy_ingestion','ingestion_snacks_frying',)


class AnthropometricForm(forms.ModelForm):
    class Meta:
        model = Anthropometric
        fields = ('patient_name', 'weight', 'pu', 'pt', 'height', 'imc', 'circ_arm', 'circ_waist', 'circ_abdomen', 'circ_hip', 'pct',
        'cmb','edema', 'age_range')


class NutriCalcForm(forms.ModelForm):
    class Meta:
        model = NutriCalc
        fields = ('patient_name','food_name')