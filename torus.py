def trunc_float(nb, size):
	i = 0
	nb = str(nb)
	a = 0
	while i < len(nb) and nb[i] != '.':
		i = i + 1
	while i < len (nb) and a < size:
		i = i + 1
		a = a + 1
	if i == len(nb):
		return (nb)
	return (nb[0:i])

def display_torus(nb, size):
	nb_round = round(nb, size)
	i = 0
	nb_round = str(nb_round)
	print("x = ", end = '')
	while i < len(nb_round) and i < size + 2:
		print(nb_round[i], end = '')
		i = i + 1
	while i < len(str(nb)) and i < size + 2:
		print('0', end = '')
		i = i + 1
	print ()

class Torus:
	def __init__(self, a, b, c, d, e):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.e = e
	def calcul(self, x):
		var = self.a * pow(x, 4)
		var = var + (self.b * pow(x, 3))
		var = var + (self.c * pow(x, 2))
		var = var + (self.d * x)
		var = var + self.e
		return (var)
	def derivee(self, x):
		var = 4 * self.a * pow(x, 3)
		var = var + (3 * self.b * pow(x, 2))
		var = var + (2 * self.c * x)
		var = var + self.d
		return(var)
