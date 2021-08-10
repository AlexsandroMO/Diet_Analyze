from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
#from .models import Employee, Project, DocumentModel, LdProj, Subject
#from .forms import ProjectForm, LdProjForm #, SubjectForm, PageTypeForm, DocTypeForm, PageformatForm, DocumentModelForm, EmployeeForm, StatusDocForm, ActionForm #, LdProjForm, CotationForm
from django.contrib import messages
#import DB_Access as db_access
from datetime import datetime


def home(request):
    data_atual = datetime.today()
    data_atual = datetime.strptime(str(data_atual)[:10], '%Y-%m-%d').date()

    stauts_body = 'page-home'

    print('>>>>>>>>>>>>> ',data_atual)

   


    return render(request,'diet/index.html', {'stauts_body': stauts_body})
