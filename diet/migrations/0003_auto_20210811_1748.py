# Generated by Django 3.2.6 on 2021-08-11 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0002_anamnesi_gender_maritalstatus_schooling'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=255, verbose_name='FAIXA ETÁRIA')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='abdominal_pain',
            field=models.TextField(blank=True, verbose_name='DOR ABDOMINAL'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='bowel_habits',
            field=models.TextField(blank=True, verbose_name='HÁBITOS INTESTINAIS'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='candy_ingestion',
            field=models.TextField(blank=True, verbose_name='INGESTÃO DE DOCES'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='cel',
            field=models.CharField(blank=True, max_length=11, verbose_name='CELULAR'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='cep',
            field=models.CharField(blank=True, max_length=8, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='city',
            field=models.CharField(blank=True, max_length=255, verbose_name='CIDADE'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='consult_motivation',
            field=models.TextField(blank=True, verbose_name='MOTIVO DA CONSULTA'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='digestion',
            field=models.TextField(blank=True, verbose_name='DIGESTÃO'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='district',
            field=models.CharField(blank=True, max_length=255, verbose_name='BAIRRO'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='email',
            field=models.CharField(blank=True, max_length=255, verbose_name='EMAIL'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='essential_foods',
            field=models.TextField(blank=True, verbose_name='ALIMENTOS INDISPENSÁVEIS'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='food_allergies',
            field=models.TextField(blank=True, verbose_name='ALERGIAS ALIMENTARES'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='frequent_infections',
            field=models.TextField(blank=True, verbose_name='INFECÇÕES FREQUENTES'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='headache',
            field=models.TextField(blank=True, verbose_name='ENXAQUECA/DOR DE CABEÇA'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='ingestion_snacks_frying',
            field=models.TextField(blank=True, verbose_name='INGESTÃO DE SALGADINHOS E FRITURAS'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='leisure_habits',
            field=models.TextField(blank=True, verbose_name='LAZER / HABITOS'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='number',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True, verbose_name='NÚMERO'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='pathologies_symptoms',
            field=models.TextField(blank=True, verbose_name='CIRURGIAS / PATOLOGIAS / SINTOMAS:'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='profession',
            field=models.CharField(blank=True, max_length=255, verbose_name='PROFISSÃO'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='schooling',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='diet.schooling', verbose_name='ESCOLARIDADE'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='skin_nail_hair',
            field=models.TextField(blank=True, verbose_name='PELE/UNHA/CABELOS'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='sleep',
            field=models.TextField(blank=True, verbose_name='SONO'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='sons',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=2, verbose_name='FILHOS'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='state',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso doSul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='ESTADO'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='street',
            field=models.CharField(blank=True, max_length=255, verbose_name='RUA'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='stress',
            field=models.TextField(blank=True, verbose_name='ESTRESSE/DEPRESSÃO'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='time_feel_hungry',
            field=models.TextField(blank=True, verbose_name='APETITE / HORÁRIO QUE SENTE MAIS FOME:'),
        ),
        migrations.AlterField(
            model_name='anamnesi',
            name='urinary_habits',
            field=models.TextField(blank=True, verbose_name='HÁBITOS URINÁRIOS'),
        ),
        migrations.CreateModel(
            name='NutriCalcResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_ptn', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='PTN')),
                ('res_gli', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='GLI')),
                ('res_lip', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='LIP')),
                ('res_ca', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Ca')),
                ('res_p', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='P')),
                ('res_fe', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Fe')),
                ('res_vit_a', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='VIT-A')),
                ('res_tia', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='TIA')),
                ('res_ribo', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='RIBO')),
                ('res_nia', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='NIA')),
                ('res_vit_c', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='VIT-C')),
                ('res_fiber', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='FIBRA')),
                ('patient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diet.anamnesi', verbose_name='PACIENTE')),
            ],
        ),
        migrations.CreateModel(
            name='NutriCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=255, verbose_name='ALIMENTOS')),
                ('qt_g', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True, verbose_name='QT')),
                ('ptn', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='PTN')),
                ('gli', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='GLI')),
                ('lip', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='LIP')),
                ('ca', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Ca')),
                ('p', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='P')),
                ('fe', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Fe')),
                ('vit_a', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='VIT-A')),
                ('tia', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='TIA')),
                ('ribo', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='RIBO')),
                ('nia', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='NIA')),
                ('vit_c', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='VIT-C')),
                ('fiber', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='FIBRA')),
                ('patient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diet.anamnesi', verbose_name='PACIENTE')),
            ],
        ),
        migrations.CreateModel(
            name='Anthropometric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='PESO ATUAL')),
                ('pu', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='PU')),
                ('pt', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='PT')),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='ALTURA')),
                ('imc', models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='IMC')),
                ('circ_arm', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='CIRC. BRAÇO')),
                ('circ_waist', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='CIRC. CINTURA')),
                ('circ_abdomen', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='CIRC. ABDOMEM')),
                ('circ_hip', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='CIRC. QUADRIL')),
                ('pct', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='PCT')),
                ('cmb', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='CMB')),
                ('edema', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='EDEMA')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('age_range', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diet.agerange', verbose_name='FAIXA ETÁRIA')),
                ('patient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diet.anamnesi', verbose_name='PACIENTE')),
            ],
        ),
    ]
