def func(*args):
	ret_values = []
	
	(n, t) = [int(x) for x in args[0].split()]
	seq = list(args[1])
	currentTime = 0
	i = 0
	while (currentTime < t):
	    while (i < (n - 1)):
	        if ((seq[i] == 'B') and (seq[(i + 1)] == 'G')):
	            seq[i] = 'G'
	            seq[(i + 1)] = 'B'
	            i += 1
	        i += 1
	    currentTime += 1
	    i = 0
	ret_values.append(''.join(seq))

	return ret_values
