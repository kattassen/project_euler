import math

target = 500
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

numbers = ["0"]*100000000
numbers = set()
target_prime = 80

for i,x in enumerate(primes[:target_prime]):
	print x
	for j,y in enumerate(primes[i+1:target_prime]):
		for k,z in enumerate(primes[i+j+2:target_prime]):
			for l,u in enumerate(primes[i+j+k+3:target_prime]):
					for pow_x in range(1,7):
						for pow_y in range(1,7):
							for pow_z in range(1,3):
								for pow_u in range(1,2):
									numbers.add((x**pow_x)*(y**pow_y)*(z**pow_z)*(u**pow_u))

numbers = list(sorted(numbers))
print "Total numbers found: " + str(len(numbers))

count = 0
for i,num in enumerate(numbers):
	if (num - 1 == numbers[i-1]):
		count += 1
	else:
		count = 0

	if count > 3:
		print (numbers[i-3])
		print (numbers[i-2])
		print (numbers[i-1])
		print (numbers[i])
		print count


#print numbers[644]
#print numbers[645]
#print "".join(numbers).find("xxxx")
