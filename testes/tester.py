from teste.teste import Teste, FalhouNoTeste


class Tester(object):

	def __init__(self):
		teste = Teste()
		self.testes = [teste]

	def teste(self):
		for teste in self.testes:
			try:
				teste.run()
			except FalhouNoTeste:
				print('O teste falhou! =(')
				return False
		print('O teste passou com sucesso!')
		return True

tester = Tester()
teste