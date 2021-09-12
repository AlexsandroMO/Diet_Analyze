from django.contrib import admin
from . models import Base, Gender, MaritalStatus, Schooling, Anamnesi, Anthropometric, NutriCalc, NutriCalcResult


class BaseAdmin(admin.ModelAdmin):
    fields = ('food_name','qt_g','ptn','gli','lip','ca','p','fe','vit_a','tia','ribo','nia','vit_c','fiber')
    list_display = ('id','food_name','qt_g','ptn','gli','lip','ca','p','fe','vit_a','tia','ribo','nia','vit_c','fiber','created_at','update_at')
    
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name_gener',)


class MaritalStatusAdmin(admin.ModelAdmin):
    list_display = ('marital_st',)


class SchoolingAdmin(admin.ModelAdmin):
    list_display = ('name_school',)


class AnamnesiAdmin(admin.ModelAdmin):
    fields = ('patient_name','cpf','age_date','gener','marital_st','sons','schooling','profession','cep','street','number','district','city','state','cel','email','consult_motivation',
    'leisure_habits','food_allergies','urinary_habits','bowel_habits','pathologies_symptoms','stress','headache',
    'frequent_infections','abdominal_pain','digestion','skin_nail_hair','sleep','time_feel_hungry','essential_foods',
    'candy_ingestion','ingestion_snacks_frying')
    list_display = ('patient_name','cpf','age_date','gener','marital_st','sons','schooling','profession','cep','street','number','district','city','state','cel','email','consult_motivation',
    'leisure_habits','food_allergies','urinary_habits','bowel_habits','pathologies_symptoms','stress','headache',
    'frequent_infections','abdominal_pain','digestion','skin_nail_hair','sleep','time_feel_hungry','essential_foods',
    'candy_ingestion','ingestion_snacks_frying','created_at','update_at')

#'patient_name',
class AnthropometricAdmin(admin.ModelAdmin):
    fields = ('patient_name', 'weight', 'pu', 'pt', 'height', 'imc', 'circ_arm', 'circ_waist', 'circ_abdomen',
    'circ_hip', 'pct', 'cmb','edema', 'age_range')
    list_display = ('id','patient_name','weight', 'pu', 'pt', 'height', 'imc', 'circ_arm', 'circ_waist','circ_abdomen',
    'circ_hip', 'pct', 'cmb', 'edema', 'age_range', 'created_at','update_at')


class NutriCalcAdmin(admin.ModelAdmin):
    fields = ('patient_name','food_name')#,'qt_g','ptn','gli','lip','ca','p','fe','vit_a','tia','ribo','nia','vit_c','fiber')
    list_display = ('id','patient_name','food_name') #,'qt_g','ptn','gli','lip','ca','p','fe','vit_a','tia','ribo','nia','vit_c','fiber')
    

class NutriCalcResultAdmin(admin.ModelAdmin):
    fields = ('patient_name','res_ptn','res_gli','res_lip','res_ca','res_p','res_fe','res_vit_a','res_tia','res_ribo','res_nia','res_vit_c','res_fiber')
    list_display = ('id','patient_name','res_ptn','res_gli','res_lip','res_ca','res_p','res_fe','res_vit_a','res_tia','res_ribo','res_nia','res_vit_c','res_fiber')

'''
class AgeRangeAdmin(admin.ModelAdmin):
    fields = ('age',)
'''

admin.site.register(Base, BaseAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(MaritalStatus, MaritalStatusAdmin)
admin.site.register(Schooling, SchoolingAdmin)
admin.site.register(Anamnesi, AnamnesiAdmin)
admin.site.register(Anthropometric, AnthropometricAdmin)
admin.site.register(NutriCalc, NutriCalcAdmin)
admin.site.register(NutriCalcResult, NutriCalcResultAdmin)
#admin.site.register(AgeRange, AgeRangeAdmin)

