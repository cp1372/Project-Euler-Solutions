f_old = 1
f_new = 2
total = 0

while (f_new < 4000000):
	if (f_new % 2 == 0):
		total += f_new
	f_new, f_old = (f_new+f_old), (f_new)

print (total)