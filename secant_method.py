def secant_method(torus, size):
	x1 = 0
	x2 = 1
	result = ((x1 - x2) / (torus.calcul(x1) - torus.calcul(x2)))
	result = result * torus.calcul(x1)
	result = x1 - result
	print("x =", result)
	while round(torus.calcul(result), size) != 0:
		if torus.calcul(result) > 0 and torus.calcul(x1) < 0:
			x2 = result
		elif torus.calcul(result) > 0 and torus.calcul(x2) < 0:
			x1 = result
		elif torus.calcul(result) < 0 and torus.calcul(x1) > 0:
			x2 = result
		else:
			x1 = result
		result = ((x1 - x2) / (torus.calcul(x1) - torus.calcul(x2)))
		result = result * torus.calcul(x1)
		result = x1 - result
		print("x =", round(result, size))
	return(result)
