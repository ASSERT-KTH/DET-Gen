def func(*args):
	
	string = args[0]
	
	def main():
	    for i in string:
	        if (i in 'HQ9'):
	            return 'YES'
	    return 'NO'
	return(main())
