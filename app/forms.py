from django import forms
from app.models import nomes, Consignado, Emprestimo

class NomesForm(forms.ModelForm):
    class Meta:
        model = nomes
        fields = [
            'Nome_completo', 'RG', 'CPF', 'Data_nascimento', 'Data_de_expedição',
            'Orgão_emiçor', 'Estado_civil', 'Nome_da_Mãe', 'Empresa',
            'Regime_de_trabalho', 'Profição', 'Salario_bruto', 'Salario_liquido',
            'Endereço_residencial', 'Numero', 'Bairro', 'Cidade', 'Estado', 'CEP',
            'imagem'
        ]

class ConsignadoForm(forms.ModelForm):
    class Meta:
        model = Consignado  # Use o modelo Consignado aqui
        fields = [
            'Status', 'Bem_do_Financiamento', 'Endereço_residencial_consignado',
            'Estado_do_Bem_consignado', 'Entrada_consignado', 'Banco_consignado',
            'Agencia_consignado', 'Conta_consignado', 'Tipo_da_conta_consignado',
            'Conclusão_consignado', 'Observação_consignado', 'RG_consignado',
            'CPF_consignado', 'Comprovante_consignado', 'IR_consignado'
        ]

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo  # Use o modelo Emprestimo aqui
        fields = [
            'Tipo_de_consignado_emprestimo', 'Valor_beneficio_renda_emprestimo',
            'Especie_de_beneficio_emprestimo', 'N_beneficio_matricula_emprestimo',
            'Margem_emprestimo', 'Banco_emprestimo', 'Agencia_emprestimo',
            'Conta_emprestimo', 'Tipo_da_conta_emprestimo', 'RG_emprestimo',
            'CPF_emprestimo', 'Comprovante_emprestimo', 'Contra_cheque_emprestimo'
        ]
