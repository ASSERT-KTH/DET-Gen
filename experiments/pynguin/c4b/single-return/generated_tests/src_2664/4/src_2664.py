def func(*args):
	
	(n, k) = map(int, args[0].split())
	diploma = ((n // 2) // (k + 1))
	gram = (diploma * k)
	s = ((n - gram) - diploma)
	return(diploma, gram, s)
