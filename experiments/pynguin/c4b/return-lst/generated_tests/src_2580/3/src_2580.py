def func(*args):
	ret_values = []
	
	n = int(args[0])
	queue = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	rotate = 0
	actQueLen = ((2 ** rotate) * 5)
	actQueNr = 0
	while (n > actQueNr):
	    actQueLen = ((2 ** rotate) * 5)
	    actQueNr = (actQueNr + actQueLen)
	    rotate += 1
	else:
	    actQueLen = ((2 ** (rotate - 1)) * 5)
	    rotate += (- 1)
	    actQueNr += (- actQueLen)
	    n += (- actQueNr)
	    for i in range(5):
	        if (n <= ((2 ** rotate) * (i + 1))):
	            ans = queue[i]
	            break
	ret_values.append(ans)

	return ret_values
