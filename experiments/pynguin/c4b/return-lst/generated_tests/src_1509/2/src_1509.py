def func(*args):
	ret_values = []
	
	y = int(args[0])
	ans = y
	for x in range((y + 1), 9999):
	    count = 0
	    for c in str(x):
	        if (str(x).count(c) > 1):
	            break
	        else:
	            count += 1
	    if (count == 4):
	        ans = x
	        break
	ret_values.append(ans)

	return ret_values
