from django.db import models

class Animais(models.Model):
    especie = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    curiosidades = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.especie}, {self.curiosidades}, {self.habitat}"

class Plantas(models.Model):
    especie = models.CharField(max_length=100)
    classe = models.CharField(max_length=100)
    reino = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.especie}, {self.classe}, {self.reino}"
    

class Ecologia(models.Model):
    nome = models.CharField(max_length=100)
    pai = models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    data_nasc = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cidades = models.ForeignKey(Cidades, on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)
    uf = models.CharField(max_length=2)
    def __str__(self):
        return f"{self.nome}, {self.cpf}, {self.ocupacao}"
    

class Biodiversidade(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nome}, {self.site}, {self.telefone}"
    

class Ecossistema(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
