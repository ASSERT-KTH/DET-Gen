def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split())
	time = (240 - k)
	
	def solved_problem(t):
	    i = 1
	    while 1:
	        if ((t - (5 * i)) < 0):
	            break
	        t = (t - (5 * i))
	        i += 1
	    return i
	x = (solved_problem(time) - 1)
	if (x > n):
	    x = n
	ret_values.append(x)

	return ret_values
