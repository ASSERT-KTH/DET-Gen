def func(*args):
	ret_values = []
	
	ns = args[0]
	s = int(ns[:(- 1)])
	m = ns[(- 1)]
	if (m == 'a'):
	    letra = 0
	if (m == 'b'):
	    letra = 1
	if (m == 'c'):
	    letra = 2
	if (m == 'd'):
	    letra = (- 1)
	if (m == 'e'):
	    letra = (- 2)
	if (m == 'f'):
	    letra = (- 3)
	if ((s % 4) == 1):
	    n = (s * 4)
	    ret_values.append((n + letra))
	if ((s % 4) == 3):
	    s = (s - 2)
	    n = (s * 4)
	    ret_values.append((n + letra))
	if ((s % 4) == 2):
	    n = ((s * 4) + 3)
	    ret_values.append((n + letra))
	if ((s % 4) == 0):
	    s = (s - 2)
	    n = ((s * 4) + 3)
	    ret_values.append((n + letra))

	return ret_values
