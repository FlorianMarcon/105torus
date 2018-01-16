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
