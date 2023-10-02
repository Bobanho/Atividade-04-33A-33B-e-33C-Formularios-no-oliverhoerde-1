from django.db import models

class Lagostas_brabas(models.Model):
  title = models.CharField(max_length=50)
  genero = models.CharField(max_length=50)
  release_date = models.DateField()
  afiliacao_partidaria = models.CharField(max_length=70)

class Agregados(models.Model):
  title = models.CharField(max_length=50)
  origem = models.CharField(max_length=100)
  CONFIABILIDADE = [
    ("0","nada confiavel"),
    ("1","confiavel o suficiente"),
    ("2","eu morreria por esse troço"),
  ]
  confia = models.CharField(max_length=1,choices=CONFIABILIDADE)

class Tabelados(models.Model):
  title = models.CharField(max_length=50)
  genero = models.CharField(max_length=50)
  preco = models.IntegerField()

# template

class Author(models.Model):
    title = models.CharField(max_length=50)
    origem = models.CharField(max_length=100)


#    def __str__(self):
#        return '{}'.format(self.name)
