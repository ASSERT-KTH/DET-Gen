def func(*args):
	ret_values = []
	
	yr = args[0]
	iter = (int(yr) + 1)
	flag = 1
	while (flag == 1):
	    unq = 1
	    arr = ([0] * 10)
	    x = list(str(iter))
	    for ch in x:
	        ch = int(ch)
	        if (arr[ch] == 0):
	            arr[ch] = 1
	        else:
	            unq = 0
	    if (unq == 1):
	        ret_values.append(str(iter))
	        break
	    iter = (iter + 1)

	return ret_values
