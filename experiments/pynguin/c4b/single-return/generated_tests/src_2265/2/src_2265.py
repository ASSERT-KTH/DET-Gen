def func(*args):
	
	w = args[0].lower()
	wf = ''
	for itch in range(0, len(w)):
	    if ((w[itch] == 'a') or (w[itch] == 'e') or (w[itch] == 'i') or (w[itch] == 'o') or (w[itch] == 'u') or (w[itch] == 'y')):
	        continue
	    else:
	        wf += ('.' + w[itch])
	return(wf)
