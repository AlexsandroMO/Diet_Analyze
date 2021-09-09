from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, patientList, editPatient, calorieCalc, calorieCalcAtualiza, editCalorieCalc

urlpatterns = [
    path('', home, name='home-home'),
    path('Patient_List', patientList, name='patient-list'),
    path('Edit_Patient/<int:id>', editPatient, name='edit-patient'),
    path('Calorie_Calc_Atualiza', calorieCalcAtualiza, name='calorie-calc-atualiza'),
    path('Calorie_Calc', calorieCalc, name='calorie-calc'),
    path('Edit_Calorie_Calc/<int:id>', editCalorieCalc, name='Edit-Calorie-Calc'),
    
     


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
