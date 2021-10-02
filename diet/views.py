from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Base, Anamnesi, NutriCalc, Anthropometric
from .forms import AnamnesiForm, AnthropometricForm, NutriCalcForm
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


def addAnamnesi(request):
    #patients = get_object_or_404(Paciente, pk=id)
    if request.method == 'POST':
        form = AnamnesiForm(request.POST)

        if form.is_valid():
            patients = form.save(commit=False)
            patients.save()
            return redirect('/Patient_List')

    else:
        form = AnamnesiForm()
        return render(request, 'diet/add-anamnesis.html', {'form': form})


def addMetric(request):
    #patients = get_object_or_404(Paciente, pk=id)
    if request.method == 'POST':
        form = AnthropometricForm(request.POST)

        if form.is_valid():
            patients = form.save(commit=False)
            patients.save()
            return redirect('/Patient_List')

    else:
        form = AnthropometricForm()
        return render(request, 'diet/add-anthropometric.html', {'form': form})


def addNutri(request, id):
    #patients = get_object_or_404(Paciente, pk=id)
    read_id = str(id)
    if request.method == 'POST':
        form = NutriCalcForm(request.POST)

        if form.is_valid():
            patients = form.save(commit=False)
            patients.save()
            return redirect('/Patient_List')

    else:
        form = NutriCalcForm()
        return render(request, 'diet/add-nutri.html', {'form': form, 'read_id ':read_id})


def choseEdit(request, id):
    stauts_body = ''

    ID = id  
    Anamnesis = Anamnesi.objects.filter(id=ID)

    return render(request,'diet/chose-edictions.html', {'stauts_body': stauts_body, 'Anamnesis':Anamnesis})    


def dataPatient(request):
    stauts_body = ''

    POST = dict(request.POST)   
    #print(POST)

    ID = int(POST['_selected_patient'][0])
    action = POST['action'][0]
    
    Metrics = Anthropometric.objects.all().order_by('patient_name')
    Bases = Base.objects.all().order_by('food_name')
    NutriCal = NutriCalc.objects.filter(patient_name_id=ID)
    read_id = ID

    if action == '0':
        return redirect('/Edit_Anamnesi/%s'%(ID))

    elif action == '1':
        return redirect('/Edit_Metric/%s'%(ID))

    elif action == '2':
        bases_read = []
        for n in NutriCal:
            #print(n.id, n.food_name_id)
            for a in Bases:
                if a.id == n.food_name_id:
                    bases_read.append([a.food_name,a.qt_g,a.ptn,a.gli,a.lip,a.ca,a.p,a.fe,a.vit_a,a.tia,a.ribo,a.nia,a.vit_c,a.fiber])

        calc_end = []
        plus0,plus1,plus2,plus3,plus4,plus5,plus6,plus7,plus8,plus9,plus10,plus11 = 0,0,0,0,0,0,0,0,0,0,0,0
        for i in bases_read:
            plus0 += i[2]
            plus1 += i[3]
            plus2 += i[4]
            plus3 += i[5]
            plus4 += i[6]
            plus5 += i[7]
            plus6 += i[8]
            plus7 += i[9]
            plus8 += i[10]
            plus9 += i[11]
            plus10 += i[12]
            plus11 += i[13]

        calc_end.append([plus0,plus1,plus2,plus3,plus4,plus5,plus6,plus7,plus8,plus9,plus10,plus11])

        return render(request,'diet/calc-calorias.html', {'stauts_body':stauts_body, 'bases_read':bases_read, 'calc_end':calc_end, 'read_id':read_id})


def editAnamnesi(request, id):
    Patients = get_object_or_404(Anamnesi, pk=id)
    form = AnamnesiForm(instance=Patients)

    status_action = True

    if request.method == 'POST':
        form = AnamnesiForm(request.POST, instance=Patients)

        if form.is_valid():
            Patients.save()
            return redirect('/Patient_List')
        else:
            return render(request, 'diet/add-anamnesis.html', {'form':form, 'Patients':Patients, 'status_action':status_action})

    else:
        return render(request, 'diet/add-anamnesis.html', {'form':form, 'Patients':Patients, 'status_action':status_action})


def editMetric(request, id):
    Patients = get_object_or_404(Anthropometric, pk=id)
    form = AnthropometricForm(instance=Patients)

    status_action = True

    if request.method == 'POST':
        form = AnthropometricForm(request.POST, instance=Patients)

        if form.is_valid():
            Patients.save()
            return redirect('/Patient_List')
        else:
            return render(request, 'diet/add-anthropometric.html', {'form': form, 'Patients': Patients, 'status_action':status_action})

    else:
        return render(request, 'diet/add-anthropometric.html', {'form': form, 'Patients': Patients, 'status_action':status_action})


def editPatientCalc(request):
    stauts_body = ''

    POST = dict(request.POST)
    print(POST)

    ID = POST['_food-name']
    read_id = POST['_patient_read'][0]

    Bases = Base.objects.all().order_by('food_name')
    NutriCal = NutriCalc.objects.filter(patient_name_id=read_id)

    return render(request,'diet/editar-calorias.html', {'stauts_body':stauts_body, 'Bases':Bases, 'NutriCal':NutriCal, 'read_id':read_id})


def calorieCalcAtualiza(request):
    stauts_body = ''

    POST = dict(request.POST)
    print(POST)

    read_id = POST['_patient_read'][0]
    id_nutri = POST['id_nutri']
    #id_nutri = ['1','3']

    Bases = Base.objects.all().order_by('food_name')
    NutriCal = NutriCalc.objects.filter(patient_name_id=read_id)

    cont = 0
    for a in NutriCal:
        print(a.patient_name, a.id)
        NutriCalcs = get_object_or_404(NutriCalc, pk=a.id)
        #print('>>>>>>>>>>>>>>>>>>>>>', a.food_name_id, int(id_nutri[cont]))
        NutriCalcs.food_name_id = int(id_nutri[cont])
        NutriCalcs.save()
        cont += 1

    return redirect('/Patient_List')
    #return render(request,'diet/calc-calorias-atualiza.html', {'stauts_body':stauts_body, 'NutriCal':NutriCal})

















'''
    
def editAnamnesi(request, id):

    PatientAnamnesis = get_object_or_404(Anamnesi, pk=id)
    form = AnamnesiForm(instance=PatientAnamnesis)

    if request.method == 'POST':
        form = AnamnesiForm(request.POST, instance=PatientAnamnesis)

        if form.is_valid():
            PatientAnamnesis.save()
            return redirect('/')

        else:
            return render(request, 'diet/editar-anamnesi.html', {'form': form, 'PatientAnamnesis': PatientAnamnesis})

    else:
        return render(request, 'diet/editar-anamnesi.html', {'form': form, 'PatientAnamnesis': PatientAnamnesis})

    
    
def editPatientxx(request, id):
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
    
    
    
    for b in range(0, len(ID)):
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
                
            return redirect('/Patient_List')
            
'''


























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
