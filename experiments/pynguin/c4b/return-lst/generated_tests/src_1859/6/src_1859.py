def func(*args):
	ret_values = []
	
	line = args[0]
	valid = True
	status = (- 1)
	username = []
	hostname = []
	resources = []
	hasResource = False
	ant = 'a'
	for e in line:
	    if (not valid):
	        break
	    if (status == (- 1)):
	        if (e.isalpha() or e.isdigit() or (e == '_')):
	            username.append(e)
	        elif (e == '@'):
	            status = 0
	        else:
	            valid = False
	    elif (status == 0):
	        if (e.isalpha() or e.isdigit() or (e == '_') or (e == '.')):
	            if ((e == '.') and (ant == '.')):
	                valid = False
	            else:
	                hostname.append(e)
	        elif (e == '/'):
	            hasResource = True
	            status = 1
	        else:
	            valid = False
	    elif (e.isalpha() or e.isdigit() or (e == '_')):
	        resources.append(e)
	    else:
	        valid = False
	    ant = e
	if ((len(username) < 1) or (len(username) > 16)):
	    valid = False
	if ((len(hostname) < 1) or (len(hostname) > 32) or (hostname[0] == '.') or (hostname[(- 1)] == '.')):
	    valid = False
	else:
	    word = ''.join(hostname).split('.')
	    for e in word:
	        if (len(e) > 16):
	            valid = False
	if (len(resources) > 16):
	    valid = False
	if (hasResource and (len(resources) < 1)):
	    valid = False
	if valid:
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
