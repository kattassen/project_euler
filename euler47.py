import math
from operator import mul

def prod(list):
	return reduce(mul, list, 1)

target = 500000
primes = [2, 3, 5, 7]

run = True
i = 10
cons_count = 0
old_i = 0


factors_count = 4
cons_target = 4

target_prod = prod(primes[:factors_count-1])

while (run):
	# Get next i
	is_prime = True
	i += 1
	factors = 0

	target_sqrt = math.sqrt(i)

	for x in primes:
		power = 0
		while(True):
			if (i % x**(power+1) == 0):
				is_prime = False
				power += 1
			else:
				break

		if (power > 0):
			#print str(x) + "   " + str(power)
			factors += 1

		if (x > target_sqrt) and (x > i/target_prod):
			break

	if factors == factors_count:
		if (i == 1 + old_i):
			#print "----- " + str (i)
			cons_count += 1

		if (cons_count == cons_target):
			for num in range(0,cons_target):
				print "##### " + str (i-num)
			break
	else:
		cons_count = 0

	old_i = i

	if (is_prime):
		primes.append(i)

	if (i >= target):
		print "Target reach"
		run = False
#print primes