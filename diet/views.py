from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Base, Anamnesi, NutriCalc
from .forms import NutriCalcForm
from django.contrib import messages
#import DB_Access as db_access
from datetime import datetime
#from geeks.models import GeeksModel
#import decimal

def home(request):
    #data_atual = datetime.today()
    #data_atual = datetime.strptime(str(data_atual)[:10], '%Y-%m-%d').date()

    stauts_body = 'page-home'

    return render(request,'diet/index.html', {'stauts_body': stauts_body})


def patientList(request):
    stauts_body = ''

    Anamnesis = Anamnesi.objects.all().order_by('patient_name')

    return render(request,'diet/clientes.html', {'stauts_body':stauts_body, 'Anamnesis':Anamnesis})    


def calorieCalc(request):
    stauts_body = '',

    POST = dict(request.POST)   
    print(POST)

    ID = int(POST['_selected_action'][0])

    Bases = Base.objects.all().order_by('food_name')
    NutriCalcs = NutriCalc.objects.filter(patient_name_id=ID)
    read_id = ID

    return render(request,'diet/calc-calorias.html', {'stauts_body':stauts_body, 'Bases':Bases,'NutriCalcs':NutriCalcs, 'read_id':read_id})


def editCalorieCalc(request, id):
    stauts_body = ''

    read_id = id
    Bases = Base.objects.all().order_by('food_name')
    NutriCalcs = get_object_or_404(NutriCalc, pk=id)
    NutriForm = NutriCalc.objects.filter(patient_name_id=id)
    form = NutriCalcForm(instance=NutriCalcs)

    base_read = []
    for a in Bases:
        print(a.id, type(a.id))
        if a.id == read_id:
            print(a.id)
            base_read.append([a.id,a.food_name,a.qt_g,a.ptn,a.gli,a.lip,a.ca,a.p,a.fe,a.vit_a,a.tia,a.ribo,a.nia,a.vit_c,a.fiber])

    print('--------------> ', base_read)

    return render(request,'diet/editar-calorias.html', {'form':form, 'NutriCalcs':NutriCalcs, 'NutriForm':NutriForm, 'Bases':Bases, 'base_read':base_read, 'read_id':read_id})


    '''if(request.method == 'POST'):
        form = NutriCalcForm(request.POST, instance=NutriCalcs)

        if(form.is_valid()):
            #if Projects.policy == '0':
                #Projects.policy = '{}000000000000{}'.format(data_atual, length)
            NutriCalcs.save()
            return redirect('/Patient_List')
        else:
            return render(request,'diet/editar-calorias.html', {'form':form, 'NutriCalcs':NutriCalcs, 'NutriForm':NutriForm, 'Bases':Bases, 'base_read':base_read})

    else:
        return render(request,'diet/editar-calorias.html', {'form':form, 'NutriCalcs':NutriCalcs, 'NutriForm':NutriForm, 'Bases':Bases, 'base_read':base_read})
    ''' 

def calorieCalcAtualiza(request):
    stauts_body = ''

    Bases = Base.objects.all().order_by('food_name')
    NutriCalcs = NutriCalc.objects.all().order_by('food_name')

    POST = dict(request.POST)
    print(POST)
    print(':::::::>>>>>>', POST['base_name'])

    ID = POST['base_name']
    read_id = int(POST['_patient_read'][0])

    base_read = []
    for a in Bases:
        for b in ID:
            if a.id == int(b):
                base_read.append([a.id,a.food_name,a.qt_g,a.ptn,a.gli,a.lip,a.ca,a.p,a.fe,a.vit_a,a.tia,a.ribo,a.nia,a.vit_c,a.fiber])

    print('--------------> ', base_read)

    NutriCalcs = get_object_or_404(NutriCalc, pk=read_id)
    form = NutriCalcForm(instance=NutriCalcs)

    if(request.method == 'POST'):
        form = NutriCalcForm(request.POST, instance=NutriCalcs)

        if(form.is_valid()):
            #if Projects.policy == '0':
                #Projects.policy = '{}000000000000{}'.format(data_atual, length)
            NutriCalcs.save()
            return redirect('/Patient_List')
        else:
            return render(request,'diet/calc-calorias-atualiza.html', {'stauts_body':stauts_body, 'Bases':Bases,'NutriCalcs':NutriCalcs,'base_read':base_read})
                #return render(request,'diet/editar-calorias.html', {'form':form, 'NutriCalcs':NutriCalcs, 'NutriForm':NutriForm, 'Bases':Bases, 'base_read':base_read})

    else:
        return render(request,'diet/calc-calorias-atualiza.html', {'stauts_body':stauts_body, 'Bases':Bases,'NutriCalcs':NutriCalcs,'base_read':base_read})
        #return render(request,'diet/editar-calorias.html', {'form':form, 'NutriCalcs':NutriCalcs, 'NutriForm':NutriForm, 'Bases':Bases, 'base_read':base_read})

    #Bases = Base.objects.filter(id=ID)
    #Bases = Base.objects.all().order_by('food_name')
    #LdProjs = LdProj.objects.filter(proj_name_id=id_proj)
    

    #return redirect('/calorie_Calc_Atualiza', {'stauts_body':stauts_body, 'Bases':Bases,'NutriCalcs':NutriCalcs,'base_read':base_read})
    return render(request,'diet/calc-calorias-atualiza.html', {'stauts_body':stauts_body, 'Bases':Bases,'NutriCalcs':NutriCalcs,'base_read':base_read})
