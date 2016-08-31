
f_new = 1
f_old = 1
n = 2
while ( len(str (f_new) ) < 1000):
	f_new, f_old = (f_old + f_new), f_new
	n = n+1
print (f_new, n)