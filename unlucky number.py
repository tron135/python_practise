for i in range(1,21):
	if i == 4 or i == 13:
		s = str(i) + " is unlucky !!!!"
		print(s)
	elif i % 2 == 0:
		t = str(i) + " is even !!"
		print(t)
	else:
		u = str(i) + " is odd !!"
		print(u)