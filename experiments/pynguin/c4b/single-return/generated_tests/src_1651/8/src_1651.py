def func(*args):
	
	a = int(args[0])
	mas = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	i = 0
	while ((5 * (2 ** i)) < a):
	    a -= (5 * (2 ** i))
	    i += 1
	kol = 1
	while (a > (2 ** i)):
	    a -= (2 ** i)
	    kol += 1
	return(mas[(kol - 1)])
