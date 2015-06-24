import math

r = 1000000

n_ = 1
d_ = 9

minimum = float(n_)/d_
maximum = float(3)/7

for potens in range(1, 6):
	for n in range(n_*10 + 1, d_*10):
		#print str(n) + " / " + str(d_*10)
		#print potens
		div = float(n)/(d_*10)
		#print(div)

		if div > maximum:
			#print "BREAK " + str(div)
			break
		minimum = div
		n_ = n

	d_ = d_*10

	for d in range(d_-1, 0, -1):
		#print str(n_) + " / " + str(d)
		#print potens

		div = float(n_)/d
		#print(div)

		if div >= maximum or div <= minimum:
			#print "BREAK " + str(div)
			break
		minimum = div
		d_ = d
		#numbers[int(str(n)+str(d))] = float(n)/d


	print "####"
	print minimum
	print n_
	print d_
#Simplify fraction
while(True):
	old_n = n_
	for i in range(2, int(math.sqrt(n_))):
		if n_%i == 0 and d_%i == 0:
			n_ = n_/i
			d_ = d_/i
	if old_n == n_:
		break
#Result

print n_
print d_


