from django.forms import ModelForm
from app.models import nomes

class NomesForm(ModelForm):
    class Meta:
        model = nomes
        fields = ['Nome_completo', 'RG', 'CPF', 'Data_nascimento', 'Data_de_expedição', 'Orgão_emiçor', 'Estado_civil', 'Nome_da_Mãe', 'Empresa', 'Regime_de_trabalho', 'Profição', 'Salario_bruto', 'Salario_liquido', 'Endereço_residencial', 'Numero', 'Bairro', 'Cidade', 'Estado', 'CEP', 'imagem']
