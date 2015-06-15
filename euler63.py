count = 0
# Only run i up to 10 since at 10 another digit is added
for i in range(1,10):
	for p in range(1,30):
		x = i**p
		if (len(str(x)) == p):
			print str(i) + "**" + str(p) + "=" + str(x)
			count += 1

print count