def func(*args):
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	drink_toast = ((k * l) // nl)
	lime_toast = (c * d)
	salt_toast = (p // np)
	return((min(drink_toast, lime_toast, salt_toast) // n))
