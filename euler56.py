sum = []

for i in range(1,100):
	for pow in range(1,100):
		s = 0
		for x in str(i**pow):
			s += int(x)
		sum.append(s)
		
print max(sum)