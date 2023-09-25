from django.db import models

# Create your models here.

def upload_imagem_nomes(instance, filename):
    return f"{instance.Nome_completo}-{filename}"
class nomes(models.Model):
    Nome_completo = models.CharField(max_length=150)
    RG = models.CharField(max_length=100)
    CPF = models.CharField(max_length=150)
    Data_nascimento = models.CharField(max_length=100)
    Data_de_expedição = models.CharField(max_length=150)
    Orgão_emiçor = models.CharField(max_length=100)
    Estado_civil = models.CharField(max_length=150)
    Nome_da_Mãe = models.CharField(max_length=100)
    Empresa = models.CharField(max_length=150)
    Regime_de_trabalho = models.CharField(max_length=100)
    Profição = models.CharField(max_length=150)
    Salario_bruto = models.CharField(max_length=100)
    Salario_liquido = models.IntegerField()
    Endereço_residencial = models.CharField(max_length=100)
    Numero = models.CharField(max_length=150)
    Bairro = models.CharField(max_length=100)
    Cidade = models.CharField(max_length=150)
    Estado = models.CharField(max_length=100)
    CEP = models.CharField(max_length=100)
    imagem = models.FileField(upload_to=upload_imagem_nomes, null=True, blank=True)