def func(*args):
	
	
	def plitki(a, b, c):
	    if (a > 1):
	        return (((plitki((a - 1), b, c) + b) + c) - 1)
	    else:
	        return (b * c)
	
	def pl(a, b, c):
	    res = (b * c)
	    for i in range((a - 1)):
	        res += ((b + c) - 1)
	    return res
	array = args[0].split(' ')
	return(pl(int(array[0]), int(array[1]), int(array[2])))
