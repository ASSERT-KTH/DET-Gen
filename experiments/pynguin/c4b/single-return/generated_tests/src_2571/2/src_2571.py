def func(*args):
	
	(a, b, c, d) = map(int, args[0].split())
	if ((abs((a - b)) < c < (a + b)) or (abs((a - b)) < d < (a + b)) or (abs((a - c)) < d < (a + c)) or (abs((b - c)) < d < (b + c))):
	    answer = 'TRIANGLE'
	elif ((abs((a - b)) <= c <= (a + b)) or (abs((a - b)) <= d <= (a + b)) or (abs((a - c)) <= d <= (a + c)) or (abs((b - c)) <= d <= (b + c))):
	    answer = 'SEGMENT'
	else:
	    answer = 'IMPOSSIBLE'
	return(answer)
