from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, patientList, addMetric, addAnamnesi, addNutri, editAnamnesi, editMetric, \
choseEdit, editPatientCalc, dataPatient, calorieCalcAtualiza

urlpatterns = [

    #----------------------------------------------------------
    path('', home, name='home-home'),
    path('Patient_List', patientList, name='patient-list'),
    
    #----------------------------------------------------------
    path('Add_Metric', addMetric, name='add-metric'),
    path('Add_Anamnesi', addAnamnesi, name='add-anamnesi'),
    path('Add_Nutri/<int:id>', addNutri, name='add-nutri'),

    #----------------------------------------------------------
    path('Edit_Anamnesi/<int:id>', editAnamnesi, name='edit-anamnesi'),
    path('Edit_Metric/<int:id>', editMetric, name='edit-metric'),

    #----------------------------------------------------------
    path('Chose_Edit/<int:id>', choseEdit, name='chose_edit'),
    path('Data_Patient', dataPatient, name='data-patient'),

    path('Calorie_Calc_Atualiza', calorieCalcAtualiza, name='calorie-calc-atualiza'),
    
    path('Edit_Patient_Calc', editPatientCalc, name='edit-patient-calc'),
    
     


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
