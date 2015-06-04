import math

target = 100
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
print primes

disctinct_no = 3
numbers = ["0"]*100000000

for i,x in enumerate(primes[:20]):
	for j,y in enumerate(primes[i:20]):
		for k,z in enumerate(primes[i+j:20]):
				#if (math.sqrt(x*y) not in primes) or (math.sqrt(z*y) not in primes) or (math.sqrt(z*x) not in primes):
				if (not x == y) and (not y == z) and (not x == z):
					print "(%d %d %d)" % (x,y,z)
					print x*y*z
					numbers[x*y*z] = "x"
				elif (x == y) and (y == z) and (x == z):
					continue
				else:
					# Since some of the parts can be set as a power to a prime, try find another factor
					for q in primes[:20]:
						#if (math.sqrt(x*q) not in primes) or (math.sqrt(z*q) not in primes) or (math.sqrt(y*q) not in primes):
						if (not x == q) and (not y == q) and (not z == q):
							print "(%d %d %d %d)" % (x,y,z,q)
							print x*y*z*q
							numbers[x*y*z*q] = "x"

#print numbers[:1000]
print numbers[644]
print numbers[645]
print numbers[646]
print "".join(numbers).find("xxx")
