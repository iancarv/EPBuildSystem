class FalhouNoTeste(Exception):
	pass

class Teste(object):
	"Classe que representa um teste generico"

	def run(self):
		if self.entrada_esperada != self.saida_esperada:
			raise FalhouNoTeste

	def entrada_esperada(self):
		return ''

	def saida_esperada(self):
		return ''


