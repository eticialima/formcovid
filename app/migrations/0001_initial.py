# Generated by Django 3.1.6 on 2021-07-15 20:59

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=150)),
                ('user_matricula', models.CharField(max_length=6)),
                ('user_empresa', models.CharField(choices=[('EMPREZA XYZ', 'EMPREZA XYZ'), ('EMPRESA ABC', 'EMPRESA ABC')], max_length=15, verbose_name='Selecione sua empresa')),
                ('user_data', models.CharField(max_length=10, verbose_name='Data de nascimento')),
                ('user_choices', models.CharField(choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=15)),
                ('user_text1', models.TextField(blank=True, max_length=100)),
                ('user_choices2', models.CharField(choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=15)),
                ('user_text2', models.TextField(blank=True, max_length=100)),
                ('user_doencas', multiselectfield.db.fields.MultiSelectField(choices=[('Febre', 'Febre'), ('Tosse', 'Tosse'), ('Dor de Garganta', 'Dor de Garganta'), ('Dificuldade de respirar', 'Dificuldade de respirar'), ('Cefaleia (Dor de cabeça)', 'Cefaleia (Dor de cabeça)'), ('Coriza', 'Coriza'), ('NÃO TENHO SINTOMAS', 'NÃO TENHO SINTOMAS')], max_length=102)),
                ('user_text3', models.TextField(blank=True, max_length=100)),
                ('user_termos', multiselectfield.db.fields.MultiSelectField(choices=[('SIM', 'SIM')], max_length=3)),
            ],
        ),
    ]
