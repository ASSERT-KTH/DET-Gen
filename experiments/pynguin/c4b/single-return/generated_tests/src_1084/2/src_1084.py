def func(*args):
	
	import math
	if (__name__ == '__main__'):
	    (n, a, b, p, q) = map(int, args[0].split())
	    if (p < q):
	        (a, b) = (b, a)
	        (p, q) = (q, p)
	    divisible_a = (n // a)
	    divisible_b = (n // b)
	    divisible_ab = (n // ((a * b) // math.gcd(a, b)))
	    return(((divisible_a * p) + ((divisible_b - divisible_ab) * q)))
