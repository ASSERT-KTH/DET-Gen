def func(*args):
	ret_values = []
	
	n = int(args[0])
	s = args[1]
	a = []
	for i in range(10):
	    a.append(True)
	for i in range(n):
	    c = int(s[i])
	    a[c] = False
	inc = 0
	if (a[1] and a[2] and a[3]):
	    inc = 3
	if (a[7] and a[9] and a[0]):
	    inc = 3
	if (a[1] and a[4] and a[7] and a[0]):
	    inc = 1
	if (a[3] and a[6] and a[9] and a[0]):
	    inc = 1
	if (inc == 0):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
