from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Base, Anamnesi, NutriCalc
from .forms import NutriCalcForm, AnamnesiForm
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


def editPatient(request, id):
    stauts_body = ''

    Patient = get_object_or_404(Anamnesi, pk=id)
    form = AnamnesiForm(instance=Patient )

    print(form)

    if(request.method == 'POST'):
        form = AnamnesiForm(request.POST, instance=Patient)

        if(form.is_valid()):
            #if Projects.policy == '0':
                #Projects.policy = '{}000000000000{}'.format(data_atual, length)
            Patient.save()
            return redirect('/Patient_List')
        else:
            return render(request,'diet/editar-paciente.html', {'form':form, 'Patient':Patient})

    else:
        return render(request,'diet/editar-paciente.html', {'form':form, 'Patient':Patient})


def calorieCalc(request):
    stauts_body = ''

    POST = dict(request.POST)   
    print(POST)

    ID = int(POST['_selected_action'][0])

    Bases = Base.objects.all()
    NutriCalcs = NutriCalc.objects.filter(patient_name_id=ID)
    read_id = ID

    return render(request,'diet/calc-calorias.html', {'stauts_body':stauts_body, 'Bases':Bases,'NutriCalcs':NutriCalcs, 'read_id':read_id})


def calorieCalcAtualiza(request):
    stauts_body = ''

    POST = dict(request.POST)

    ID = POST['food_name']
    read_id = POST['_patient_read'][0]
    id_nutri = POST['id_nutri']

    Bases = Base.objects.all().order_by('food_name')
    NutriCal = NutriCalc.objects.filter(patient_name_id=read_id)

    cont = 0
    for a in NutriCal:
        print(a.patient_name)
        NutriCalcs = get_object_or_404(NutriCalc, pk=id_nutri[cont])
        NutriCalcs.food_name_id = int(ID[cont])
        NutriCalcs.save()
        cont += 1

    return render(request,'diet/calc-calorias-atualiza.html', {'stauts_body':stauts_body, 'Bases':Bases,'NutriCal':NutriCal})






















        #a.food_name = int(ID[b])

        #for a in range(0, len(ID)):
    '''for b in range(0, len(ID)):
        if a.id == int(ID[b]):
            base_read.append([a.id,a.food_name,a.qt_g,a.ptn,a.gli,a.lip,a.ca,a.p,a.fe,a.vit_a,a.tia,a.ribo,a.nia,a.vit_c,a.fiber])
            print('--------------------------------------- foi até aqui')

            print('test----------------------------======>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> : ',NutriCalcs[int(ID[b])].food_name_id)
            #NutriCalcs[int(ID[b])].patient_name = int(ID[b])

            NutriCalcs = get_object_or_404(NutriCalc, pk=int(ID[b]))
            #form = NutriCalcForm(instance=NutriCalcs)

            if(request.method == 'POST'):
                form = NutriCalcForm(request.POST, instance=NutriCalcs)
                print('--------------------------------------- entrou aqui')
                #if(form.is_valid()):
                print('--------------------------------------- entrou aqui tb')
                #if Projects.policy == '0':
                    #Projects.policy = '{}000000000000{}'.format(data_atual, length)
                NutriCalcs.food_name_id = int(ID[b])
                NutriCalcs.save()
                #return redirect('/Patient_List')
                print('>>>>>>>>>>>>>>>>>>>>>>> Feito')
                
            return redirect('/Patient_List')'''
            #return render(request,'diet/calc-calorias-atualiza.html', {'stauts_body':stauts_body, 'Bases':Bases,'NutriCalcs':NutriCalcs,'base_read':base_read, 'form':form})
                #else:
                    #return render(request,'diet/calc-calorias-atualiza.html', {'stauts_body':stauts_body, 'Bases':Bases,'NutriCalcs':NutriCalcs,'base_read':base_read, 'form':form})

    #else:
 


























def calorieCalcAtualizaxxx(request):
    stauts_body = ''

    Bases = Base.objects.all().order_by('food_name')
    NutriCalcs = NutriCalc.objects.all().order_by('food_name')

    POST = dict(request.POST)
    print(POST)
    print(':::::::>>>>>>', POST['food_name'])

    ID = POST['food_name']
    read_id = POST['_patient_read'][0]

    base_read = []
    for a in Bases:
        for b in ID:
            if a.id == int(b):
                base_read.append([a.id,a.food_name,a.qt_g,a.ptn,a.gli,a.lip,a.ca,a.p,a.fe,a.vit_a,a.tia,a.ribo,a.nia,a.vit_c,a.fiber])

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
            return render(request,'diet/calc-calorias-atualiza.html', {'stauts_body':stauts_body, 'Bases':Bases,'NutriCalcs':NutriCalcs,'base_read':base_read, 'form':form})

    else:
        return render(request,'diet/calc-calorias-atualiza.html', {'stauts_body':stauts_body, 'Bases':Bases,'NutriCalcs':NutriCalcs,'base_read':base_read, 'form':form})















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
