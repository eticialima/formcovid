from django.db import models 
from multiselectfield import MultiSelectField
from django import forms

# CHOICES DO FIELD DA EMPRESA  
CHOICES_EMPRESA = (
        ('EMPREZA XYZ', 'EMPREZA XYZ'),
        ('EMPRESA ABC', 'EMPRESA ABC'),
    )

CHOICES=[('SIM','SIM'),
         ('NÃO','NÃO')]

TESTE=(('Febre', 'Febre'),
        ('Tosse', 'Tosse'),
        ('Dor de Garganta', 'Dor de Garganta'),
        ('Dificuldade de respirar', 'Dificuldade de respirar'),
        ('Cefaleia (Dor de cabeça)', 'Cefaleia (Dor de cabeça)'),
        ('Coriza', 'Coriza'),
        ('NÃO TENHO SINTOMAS', 'NÃO TENHO SINTOMAS'),
 )

TESTE2=[('SIM','SIM')]
 
class cadastro(models.Model):
    user_name = models.CharField(max_length=150)
    user_matricula = models.CharField(max_length=6)
    user_empresa = models.CharField('Selecione sua empresa', max_length=15, choices=CHOICES_EMPRESA, blank=False, null=False)
    user_data = models.CharField('Data de nascimento', max_length=10)  
    user_choices = models.CharField(max_length=15, choices=CHOICES) 
    user_text1=models.TextField(max_length=100,  blank=True )  
    user_choices2 = models.CharField(max_length=15, choices=CHOICES) 
    user_text2=models.TextField(max_length=100,  blank=True )  
    user_doencas = MultiSelectField(choices=TESTE)
    user_text3=models.TextField(max_length=100,  blank=True )  
    user_termos=MultiSelectField(choices=TESTE2) 
  