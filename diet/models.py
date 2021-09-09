from django.db import models
from django.contrib.auth import get_user_model


class Base(models.Model): #Base

    food_name = models.CharField(max_length=255, verbose_name='ALIMENTOS')
    qt_g = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True, verbose_name='QT')
    ptn = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='PTN')
    gli = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='GLI')
    lip = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='LIP')
    ca = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='Ca')
    p = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='P')
    fe = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='Fe')
    vit_a = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='VIT-A')
    tia = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='TIA')
    ribo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='RIBO')
    nia = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='NIA')
    vit_c = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='VIT-C')
    fiber = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='FIBRA')
    #Registro de entrada
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.food_name


class Gender(models.Model): #Gênero
    name_gener = models.CharField(max_length=255, verbose_name='GÊNERO')
    #Registro de entrada
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_gener


class MaritalStatus(models.Model): #Gênero
    marital_st = models.CharField(max_length=255, verbose_name='ESTADO CIVIL')
    #Registro de entrada
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.marital_st


class Schooling(models.Model): #Gênero
    name_school = models.CharField(max_length=255, verbose_name='ESCOLARIDADES')
    #Registro de entrada
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_school
        

'''class AgeRange(models.Model): #Gênero
    age = models.CharField(max_length=255, verbose_name='FAIXA ETÁRIA')
    #Registro de entrada
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.age'''

    
class Anamnesi(models.Model): #ANAMNESE
    STATE_NAME = (
        ('AC','Acre'),
        ('AL','Alagoas'),
        ('AP','Amapá'),
        ('AM','Amazonas'),
        ('BA','Bahia'),
        ('CE','Ceará',),
        ('DF','Distrito Federal'),
        ('ES','Espírito Santo'),
        ('GO','Goiás'),
        ('MA','Maranhão'),
        ('MT','Mato Grosso'),
        ('MS','Mato Grosso doSul'),
        ('MG','Minas Gerais'),
        ('PA','Pará'),
        ('PB','Paraíba'),
        ('PR','Paraná'),
        ('PE','Pernambuco'),
        ('PI','Piauí'),
        ('RJ','Rio de Janeiro'),
        ('RN','Rio Grande do Norte'),
        ('RS','Rio Grande do Sul'),
        ('RO','Rondônia'),
        ('RR','Roraima'),
        ('SC','Santa Catarina'),
        ('SP','São Paulo'),
        ('SE','Sergipe'),
        ('TO','Tocantins'),
    )
    #----------------------------------------------Dados Cadastrais----------------------------
    patient_name = models.CharField(max_length=255, verbose_name='NOME DO PACIENTE')
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    age_date = models.DateField(blank=True, null=True, verbose_name='DATA DE NASCIMENTO')
    gener = models.ForeignKey(Gender, on_delete=models.CASCADE, verbose_name='GÊNERO')
    marital_st = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE, verbose_name='ESTADO CIVIL')
    sons = models.DecimalField(max_digits=2, decimal_places=0, verbose_name='FILHOS')
    schooling = models.ForeignKey(Schooling, on_delete=models.CASCADE, blank=True, null=False, verbose_name='ESCOLARIDADE')
    profession = models.CharField(max_length=255, blank=True, null=False, verbose_name='PROFISSÃO')
    #----------------------------------------------Endereço------------------------------------
    cep = models.CharField(max_length=8, blank=True, null=False, verbose_name='CEP')
    street = models.CharField(max_length=255, blank=True, null=False, verbose_name='RUA')
    number = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True, verbose_name='NÚMERO')
    district = models.CharField(max_length=255, blank=True, null=False, verbose_name='BAIRRO')
    city = models.CharField(max_length=255, blank=True, null=False, verbose_name='CIDADE')
    state = models.CharField(
        max_length=2,
        choices=STATE_NAME, verbose_name='ESTADO'
        )
    #----------------------------------------------Email------------------------------------
    cel = models.CharField(max_length=11, blank=True, null=False, verbose_name='CELULAR')
    email = models.CharField(max_length=255, blank=True, null=False, verbose_name='EMAIL')
    #----------------------------------------------Patologias------------------------------------
    consult_motivation = models.TextField(blank=True, null=False, verbose_name='MOTIVO DA CONSULTA')
    leisure_habits = models.TextField(blank=True, null=False, verbose_name='LAZER / HABITOS')
    food_allergies = models.TextField(blank=True, null=False, verbose_name='ALERGIAS ALIMENTARES')
    urinary_habits = models.TextField(blank=True, null=False, verbose_name='HÁBITOS URINÁRIOS')
    bowel_habits = models.TextField(blank=True, null=False, verbose_name='HÁBITOS INTESTINAIS')
    pathologies_symptoms = models.TextField(blank=True, null=False, verbose_name='CIRURGIAS / PATOLOGIAS / SINTOMAS:')
    stress = models.TextField(blank=True, null=False, verbose_name='ESTRESSE/DEPRESSÃO')
    headache = models.TextField(blank=True, null=False, verbose_name='ENXAQUECA/DOR DE CABEÇA')
    frequent_infections = models.TextField(blank=True, null=False, verbose_name='INFECÇÕES FREQUENTES')
    abdominal_pain = models.TextField(blank=True, null=False, verbose_name='DOR ABDOMINAL')
    digestion = models.TextField(blank=True, null=False, verbose_name='DIGESTÃO')
    skin_nail_hair = models.TextField(blank=True, null=False, verbose_name='PELE/UNHA/CABELOS')
    sleep = models.TextField(blank=True, null=False, verbose_name='SONO')
    #-----------------------------------------------Hábtos-----------------------------------
    time_feel_hungry = models.TextField(blank=True, null=False, verbose_name='APETITE / HORÁRIO QUE SENTE MAIS FOME:')
    essential_foods = models.TextField(blank=True, null=False, verbose_name='ALIMENTOS INDISPENSÁVEIS')
    candy_ingestion = models.TextField(blank=True, null=False, verbose_name='INGESTÃO DE DOCES')
    ingestion_snacks_frying = models.TextField(blank=True, null=False, verbose_name='INGESTÃO DE SALGADINHOS E FRITURAS')
    #Registro de entrada
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient_name


class Anthropometric(models.Model): #AVALIAÇÃO ANTROPOMÉTRICA
    STATUS_AGE = (
        ('A','Criança 0 a 5 Anos'),
        ('B','Criança 6 a 10 Anos'),
        ('C','Adolescente 11 a 19 Anos'),
        ('D','Adulto'),
    )
    patient_name = models.ForeignKey(Anamnesi, on_delete=models.CASCADE, verbose_name='PACIENTE')
    #Adultos
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PESO ATUAL')
    pu = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PU')
    pt = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PT')
    height = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='ALTURA')
    imc = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='IMC')
    circ_arm = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='CIRC. BRAÇO')
    circ_waist = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='CIRC. CINTURA')
    circ_abdomen = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='CIRC. ABDOMEM')
    circ_hip = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='CIRC. QUADRIL')
    pct = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PCT')
    cmb = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='CMB')
    edema = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='EDEMA')
    #FAIXA ETÁRIA
    age_range = models.CharField(
        max_length=2,
        choices=STATUS_AGE, verbose_name='FAIXA ETÁRIA'
        )
    #age_range = models.ForeignKey(AgeRange, on_delete=models.CASCADE, verbose_name='FAIXA ETÁRIA')
    #Registro de entrada
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    #def __str__(self):
       #return self.weight


class NutriCalc(models.Model): #Calculo Nutricional

    patient_name = models.ForeignKey(Anamnesi, on_delete=models.CASCADE, verbose_name='PACIENTE')
    food_name = models.ForeignKey(Base, on_delete=models.CASCADE, verbose_name='ALIMENTO')
    #food_name = models.CharField(max_length=255, verbose_name='ALIMENTOS')
    qt_g = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True, verbose_name='QT')
    ptn = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='PTN')
    gli = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='GLI')
    lip = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='LIP')
    ca = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='Ca')
    p = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='P')
    fe = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='Fe')
    vit_a = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='VIT-A')
    tia = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='TIA')
    ribo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='RIBO')
    nia = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='NIA')
    vit_c = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='VIT-C')
    fiber = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='FIBRA')

    #def __str__(self):
        #return self.food_name

class NutriCalcResult(models.Model): #Resultado Calculo Nutricional

    patient_name = models.ForeignKey(Anamnesi, on_delete=models.CASCADE, verbose_name='PACIENTE')
    res_ptn = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='PTN')
    res_gli = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='GLI')
    res_lip = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='LIP')
    res_ca = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='Ca')
    res_p = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='P')
    res_fe = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='Fe')
    res_vit_a = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='VIT-A')
    res_tia = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='TIA')
    res_ribo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='RIBO')
    res_nia = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='NIA')
    res_vit_c = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='VIT-C')
    res_fiber = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='FIBRA')

    #def __str__(self):
        #return self.res_ptn





        #fiber = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='FIBRA')







'''class Laboratory(models.Model): #Base

    patient_name = models.CharField(max_length=255, verbose_name='ALIMENTOS')
    email = models.ForeignKey(Pageformat, on_delete=models.CASCADE)
   
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.food_name'''




#height_kids = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='ALTURA')
#age_kids = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='EDEMA')
#weight_kids = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='EDEMA')
#imc_kids = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='EDEMA')
