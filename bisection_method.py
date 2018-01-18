from torus import *
from math import trunc

def bisection_method(torus, size):
	var1 = 0
	var2 = 1
	result = 0.5
	while round(torus.calcul(result), size) != 0:
		print ("x =", trunc_float(result, size + 1))
		if torus.calcul(result) > 0 and torus.calcul(var2) < 0:
			var1 = result
		elif torus.calcul(result) < 0 and torus.calcul(var2) > 0:
			var1 = result
		else:
			var2 = result
		result = (var2 + var1) / 2
