def func(*args):
	
	(c, v0, v1, a, l) = list(map(int, args[0].split()))
	aux = v0
	i = 1
	while (c > aux):
	    aux += min((v0 + (i * a)), v1)
	    i += 1
	    aux -= l
	return(i)
