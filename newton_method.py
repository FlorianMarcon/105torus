from torus import *

def newton_method(torus, size):
	x = 0.5
	display_torus(x, size)
	while round(torus.calcul(x), size) != 0:
		x = x - (torus.calcul(x) / torus.derivee(x))
		display_torus(x, size)
	return (x)
