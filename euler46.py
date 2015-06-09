import math

target = 6000
primes = [2, 3, 5, 7]

run = True
i = 7
while (run):
	# Get next i
	i += 1

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
		run = False
#print primes

numbers = ["."]*1000000

for x in primes:
	# Mark the prime
	numbers[x] = "X"
	for i in range(1,250):
		numbers[x+(2*(i**2))]= "x"

print "".join(numbers).find("...")+1