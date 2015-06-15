count = 0

for i in range(1,10000000):
	curr_num = i
	while (True):

		num = 0
		for d in (str(curr_num)):
			num = int(d)**2 + num
		
		if num == 1:
			break
	 	elif num == 89:
			count += 1
			#print i
			break

		curr_num = num
	
print count