def func(*args):
	
	
	def readln():
	    return tuple(map(int, args[0].split()))
	(x, y) = readln()
	x *= 100
	y *= 10
	_ = 0
	while ((x + y) >= 220):
	    if (_ == 0):
	        if (x >= 200):
	            x -= 200
	            y -= 20
	        elif (x == 100):
	            x -= 100
	            y -= 120
	        else:
	            y -= 220
	    elif (y >= 220):
	        y -= 220
	    elif (y >= 120):
	        y -= 120
	        x -= 100
	    else:
	        y -= 20
	        x -= 200
	    if ((x < 0) or (y < 0)):
	        break
	    _ = ((_ + 1) % 2)
	return(('Hanako' if (not _) else 'Ciel'))
