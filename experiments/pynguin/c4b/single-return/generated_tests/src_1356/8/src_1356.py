def func(*args):
	
	from time import sleep
	a = sorted(list(map(int, args[0].split()))[1:])
	s = 0
	for i in range(1000):
	    for j in range(1000):
	        for k in range(5):
	            s += ((i * j) * k)
	return(' '.join(map(str, a)))
