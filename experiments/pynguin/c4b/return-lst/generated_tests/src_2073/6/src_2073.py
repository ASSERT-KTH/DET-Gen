def func(*args):
	ret_values = []
	
	
	def seperateints(x):
	    k = ''
	    l = []
	    for i in x:
	        if (i == ' '):
	            l.append(int(k))
	            k = ''
	            continue
	        k = (k + i)
	    l.append(int(k))
	    return l
	
	def luckynum(x):
	    for i in x:
	        if ((i != '4') and (i != '7')):
	            return False
	    return True
	n = int(args[0])
	i = 5
	while (n > i):
	    n -= i
	    i *= 2
	x = (i / 5)
	nn = 0
	k = 0
	while (k < n):
	    k = (k + x)
	    nn += 1
	if (nn == 1):
	    ret_values.append('Sheldon')
	elif (nn == 2):
	    ret_values.append('Leonard')
	elif (nn == 3):
	    ret_values.append('Penny')
	elif (nn == 4):
	    ret_values.append('Rajesh')
	elif (nn == 5):
	    ret_values.append('Howard')

	return ret_values
