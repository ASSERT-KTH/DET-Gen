def func(*args):
	
	a = int(args[0])
	a = list(str(a))
	T = 'YES'
	H = 0
	for x in a:
	    if ((x != '4') and (x != '7')):
	        H = H
	    else:
	        H = (H + 1)
	H = list(str(H))
	if (T == 'YES'):
	    for x in H:
	        if ((x != '4') and (x != '7')):
	            T = 'NO'
	return(T)
