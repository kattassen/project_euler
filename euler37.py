import math

target = 800000
primes = [2, 3, 5, 7]

run = True
i = 7
while (run):
	# Get next i
	i += 1

	#print "I " + str(i)

	if (i % 2 == 0):
		continue

	is_prime = True
	for x in primes:
		#print "X " + str(x)
		if (i % x == 0):
			is_prime = False
			break

		if (x > math.sqrt(i)):
			break
	
	if (is_prime):
		primes.append(i)

	if (i >= target):
		print "Target reach"
		run = False

#print primes

left_truncable = [2,3,5,7]
for p in primes:
	# Check if left truncable
	# 2,3,5,7 is not considered truncable
	if (p <= 7):
		continue
	
	if int(str(p)[0:-1]) in left_truncable:
		left_truncable.append(p)

right_truncable = [2,3,5,7]
for p in primes:
	# Check if right truncable
	# 2,3,5,7 is not considered truncable
	if (p <= 7):
		continue
	
	if int(str(p)[1:]) in right_truncable:
		right_truncable.append(p)


#print left_truncable
#print right_truncable

truncable = []
for x in left_truncable:
	if x in right_truncable:
		truncable.append(x)
print sum(truncable[4:])