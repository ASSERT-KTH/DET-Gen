def func(*args):
	
	a = [int(x) for x in args[0].split(' ')]
	b = []
	b.append(((a[1] * 2) + (a[2] * 2)))
	b.append(((a[0] * 2) + (a[2] * 2)))
	b.append(((a[0] * 2) + (a[1] * 2)))
	b.append(((a[0] + a[1]) + a[2]))
	return(min(b))
