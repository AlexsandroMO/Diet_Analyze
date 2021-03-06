# Generated by Django 3.2.6 on 2021-08-11 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_gener', models.CharField(max_length=255, verbose_name='GÊNERO')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marital_st', models.CharField(max_length=255, verbose_name='ESTADO CIVIL')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schooling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_school', models.CharField(max_length=255, verbose_name='ESCOLARIDADES')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Anamnesi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=255, verbose_name='NOME DO PACIENTE')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('age_date', models.DateField(blank=True, null=True, verbose_name='DATA DE NASCIMENTO')),
                ('sons', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True, verbose_name='FILHOS')),
                ('profession', models.CharField(max_length=255, verbose_name='PROFISSÃO')),
                ('cep', models.CharField(max_length=255, verbose_name='CEP')),
                ('street', models.CharField(max_length=255, verbose_name='RUA')),
                ('number', models.CharField(max_length=255, verbose_name='NÚMERO')),
                ('district', models.CharField(max_length=255, verbose_name='BAIRRO')),
                ('city', models.CharField(max_length=255, verbose_name='CIDADE')),
                ('state', models.CharField(max_length=255, verbose_name='ESTADO')),
                ('cel', models.CharField(max_length=255, verbose_name='CELULAR')),
                ('email', models.CharField(max_length=255, verbose_name='EMAIL')),
                ('consult_motivation', models.TextField(verbose_name='MOTIVO DA CONSULTA')),
                ('leisure_habits', models.TextField(verbose_name='LAZER / HABITOS')),
                ('food_allergies', models.TextField(verbose_name='ALERGIAS ALIMENTARES')),
                ('urinary_habits', models.TextField(verbose_name='HÁBITOS URINÁRIOS')),
                ('bowel_habits', models.TextField(verbose_name='HÁBITOS INTESTINAIS')),
                ('pathologies_symptoms', models.TextField(verbose_name='CIRURGIAS / PATOLOGIAS / SINTOMAS:')),
                ('stress', models.TextField(verbose_name='ESTRESSE/DEPRESSÃO')),
                ('headache', models.TextField(verbose_name='ENXAQUECA/DOR DE CABEÇA')),
                ('frequent_infections', models.TextField(verbose_name='INFECÇÕES FREQUENTES')),
                ('abdominal_pain', models.TextField(verbose_name='DOR ABDOMINAL')),
                ('digestion', models.TextField(verbose_name='DIGESTÃO')),
                ('skin_nail_hair', models.TextField(verbose_name='PELE/UNHA/CABELOS')),
                ('sleep', models.TextField(verbose_name='SONO')),
                ('time_feel_hungry', models.TextField(verbose_name='APETITE / HORÁRIO QUE SENTE MAIS FOME:')),
                ('essential_foods', models.TextField(verbose_name='ALIMENTOS INDISPENSÁVEIS')),
                ('candy_ingestion', models.TextField(verbose_name='INGESTÃO DE DOCES')),
                ('ingestion_snacks_frying', models.TextField(verbose_name='INGESTÃO DE SALGADINHOS E FRITURAS')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('gener', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diet.gender', verbose_name='GÊNERO')),
                ('marital_st', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diet.maritalstatus', verbose_name='ESTADO CIVIL')),
                ('schooling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diet.schooling', verbose_name='ESCOLARIDADE')),
            ],
        ),
    ]
