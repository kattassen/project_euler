import math
start = int(math.sqrt(1020304050607080900))
stop = int(math.sqrt(1929394959697989990))

while (True):
	p = start**2

	found = True
	if p % 10 == 0:
		for digit in reversed(range(2, 19, 2)):
			#print "   " + str((p / 10**digit) % 10) + "   " + str((20-digit)/2) + "    " + str(digit)

			if not ((p / 10**digit) % 10) == (20-digit)/2:
				found = False
				break

		if found:
			print p

	start += 1
	if (start == stop):
		break