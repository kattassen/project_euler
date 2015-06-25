import math
old_num = 0
best_line = 0
f = open("p099_base_exp.txt")
for line in f:
	print line
	x = int(line.split(',')[1]) * math.log(int(line.split(',')[0]))
	if x > old_num:
		print "best so far!"
		old_num = x
		best_line = line

print "#####"
print best_line
