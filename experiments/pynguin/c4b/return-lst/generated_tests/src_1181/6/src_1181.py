def func(*args):
	ret_values = []
	
	
	def f(x):
	    return ((x * (x + 1)) // 2)
	
	def works(n, k, s):
	    rem = ((k - 1) - s)
	    val = ((f((k - 1)) - f(rem)) + 1)
	    return (val >= n)
	
	def main():
	    (n, k) = map(int, args[0].split())
	    if (n == 1):
	        ret_values.append(0)
	    elif (not works(n, k, k)):
	        ret_values.append((- 1))
	    else:
	        lo = 0
	        hi = k
	        while ((lo + 1) < hi):
	            mid = ((lo + hi) // 2)
	            if works(n, k, mid):
	                hi = mid
	            else:
	                lo = mid
	        ret_values.append(hi)
	main()

	return ret_values
