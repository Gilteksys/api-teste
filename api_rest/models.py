from django.db import models

class Cliente(models.Model):
	nome = models.CharField(max_length = 200)
	endereco = models.CharField(max_length=300)
	documento = models.CharField(max_length=18)	
	contato = models.CharField(max_length=15)
	descricao = models.TextField()

	def __str__(self):
		return self.nome


