def func(*args):
	
	
	def gcd(a, b):
	    if (b == 0):
	        return a
	    return gcd(b, (a % b))
	(a, b, n) = map(int, args[0].split())
	sa = [a, b]
	Ans = True
	while (n > 0):
	    Ans = (not Ans)
	    n -= gcd(sa[Ans], n)
	return(int(Ans))
