#3

#Compute c1=c2 
#when c1 % n1 = a1
# and c2 % n2 = a2
def solveTwomodularEquations(n1, a1, n2, a2):
	multiple = 1
	c1 = a1%n1
	c2 = a2%n2

	while c1 != c2:
		c1 += n1
		c2 += n2

		if c1 % n1 != a1:
			print "HELL NO"
			break

		print c1
		print c2
		raw_input()
		multiple += 1

	print "Inter: " , c1
	return c1


solveTwomodularEquations(7, 2, 7, 6)