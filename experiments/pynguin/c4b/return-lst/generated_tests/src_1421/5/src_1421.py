def func(*args):
	ret_values = []
	
	x = args[0]
	x = ' '.join(x)
	x = x.split()
	y = 0
	na = 8
	suma = 0
	mensaje = 'NO'
	for s in range((len(x) - 6)):
	    for m in range((s + 1), (s + 7)):
	        if (x[s] != x[m]):
	            break
	        suma = (suma + 1)
	        if (suma == 6):
	            break
	    if (suma == 6):
	        mensaje = 'YES'
	        break
	    suma = 0
	ret_values.append(mensaje)

	return ret_values
