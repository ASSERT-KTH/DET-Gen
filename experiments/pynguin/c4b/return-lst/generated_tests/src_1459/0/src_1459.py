def func(*args):
	ret_values = []
	
	x = int(args[0])
	m = (x + 1)
	q = 0
	w = 0
	e = 0
	r = 0
	while (m < 9013):
	    q = int((m / 1000))
	    w = int(((m - (q * 1000)) / 100))
	    e = int((((m - (q * 1000)) - (w * 100)) / 10))
	    r = int((((m - (q * 1000)) - (w * 100)) - (e * 10)))
	    if ((q == w) or (q == e) or (q == r) or (w == e) or (w == r) or (e == r)):
	        m = (m + 1)
	    else:
	        ret_values.append(m)
	        break

	return ret_values
