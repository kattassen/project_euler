
perimeter = 1001

p = [0] * (perimeter + 1);

for x in range(1, perimeter-1):
	x_sqr = pow(x,2)
	for y in range(x, perimeter-x):
		y_sqr = pow(y,2)
		for z in range(y, perimeter-y):
			#print "-------------"
			#print y
			#print z
			#print x+y+z

			if (x+y+z > perimeter):
				break;

			z_sqr = pow(z,2)

			if sorted([x_sqr,y_sqr,z_sqr])[2] == (sorted([x_sqr,y_sqr,z_sqr])[0] + sorted([x_sqr,y_sqr,z_sqr])[1]):
				p[x+y+z] += 1
			
print p.index(max(p))