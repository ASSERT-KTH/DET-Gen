def func(*args):
	
	import sys
	sys.setrecursionlimit(3000)
	
	def sigma(i, n):
	    if (i == 1):
	        return (n - 1)
	    else:
	        return ((i * (n - i)) + sigma((i - 1), n))
	n = int(args[0])
	ans = (sigma(n, n) + n)
	return(ans)
