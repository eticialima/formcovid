from django.forms import ModelForm
from app.models import cadastro 
# Create the form class.
class cadastroForm(ModelForm):
    class Meta:
        model = cadastro
        fields = [ 'user_name', 'user_matricula', 'user_empresa','user_data', 'user_choices', 'user_text1','user_choices2', 'user_text2',  'user_doencas', 'user_text3', 'user_termos' ] 
        
     