from torus import *

def newton_method(torus, size):
	x = 0.5
	while round(torus.calcul(x), size) != 0:
		x = x - (torus.calcul(x) / torus.derivee(x))
		print("x =", trunc_float(x, size + 1))
	return (x)
