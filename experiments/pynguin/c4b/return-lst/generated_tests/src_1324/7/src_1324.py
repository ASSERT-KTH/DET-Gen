def func(*args):
	ret_values = []
	
	
	def cnt(s, v):
	    ans = 0
	    for i in s:
	        if (i == v):
	            ans += 1
	    if (ans < 2):
	        return 0
	    if (ans > 3):
	        return 3
	    return ans
	s = [int(z) for z in args[0].split()]
	mx = 0
	for i in range(1000):
	    mx = max(mx, (cnt(s, i) * i))
	ret_values.append((sum(s) - mx))

	return ret_values
