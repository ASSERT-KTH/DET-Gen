def func(*args):
	ret_values = []
	
	(a, b) = [int(x) for x in args[0].split()]
	(c, d) = [int(x) for x in args[1].split()]
	current = min(b, d)
	if (current == b):
	    inc = a
	    sub = d
	    mod = c
	else:
	    inc = c
	    sub = b
	    mod = a
	done = False
	for i in range(100000):
	    if ((current >= sub) and (((current - sub) % mod) == 0)):
	        firstanswer = current
	        done = True
	        break
	    else:
	        current += inc
	if (not done):
	    firstanswer = float('inf')
	current = max(b, d)
	if (current == b):
	    inc = a
	    sub = d
	    mod = c
	else:
	    inc = c
	    sub = b
	    mod = a
	done = False
	for i in range(100000):
	    if ((current >= sub) and (((current - sub) % mod) == 0)):
	        secondanswer = current
	        done = True
	        break
	    else:
	        current += inc
	if (not done):
	    secondanswer = float('inf')
	if ((firstanswer == float('inf')) and (secondanswer == float('inf'))):
	    ret_values.append((- 1))
	else:
	    ret_values.append(min(firstanswer, secondanswer))

	return ret_values
