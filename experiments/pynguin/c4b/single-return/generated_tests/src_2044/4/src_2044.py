def func(*args):
	
	(m, d) = map(int, args[0].split())
	if (m == 2):
	    k = 28
	elif ((m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 8) or (m == 10) or (m == 12)):
	    k = 31
	else:
	    k = 30
	broj_tjedana = 1
	nedjelja = ((7 - d) + 1)
	while (nedjelja < k):
	    broj_tjedana += 1
	    nedjelja += 7
	return(broj_tjedana)
