def func(*args):
	ret_values = []
	
	i = input
	a = i()
	b = i()
	c = str((int(a) + int(b)))
	a = a.replace('0', '')
	b = b.replace('0', '')
	c = c.replace('0', '')
	ret_values.append(('YES' if ((int(a) + int(b)) == int(c)) else 'NO'))

	return ret_values
