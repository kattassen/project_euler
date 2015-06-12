import math
start = int(math.sqrt(1020304050607080900))
stop = int(math.sqrt(1929394959697989990))

while (True):
	p = start**2

	if (p % 10 == 0):
		loops = 0

		found = True
		for i in range(2,18,2):
			#print "JKJK " + str(p)[i] + "  " + str(i-loops) + "   " + str(loops)
			if not (str(p)[i] == str(i-loops)):
				found = False
				break
			else:
				print str(p) + "    "+ str(loops)
				loops += 1
				

		if (found == True):
			print p
			

	if start == stop:
		break

	start += 1
