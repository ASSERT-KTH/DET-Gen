def func(*args):
	
	var = list(map(int, args[0].split()))
	i = 0
	while 1:
	    i += 1
	    var[0] *= 3
	    var[1] *= 2
	    if (var[0] > var[1]):
	        break
	return(i)
