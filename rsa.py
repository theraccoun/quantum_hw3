#3

n = 640434271860669796692811836922138143942513719203565769421924022297363333847089887235971007435680486193657059 
e1 = 65537 
e2 = 65539 
c1 = 400030256839145194441034228199292487980894977737102147552044462667917219509871638663296814615652770720888715 
c2 = 48384876797138828670281479166255073593234801358795810198774095180850824157124747742456773738763877257747936

import math

def solve_rsa():
	M = math.log(c2)
	mod = math.log(n)

	raw_input()
	while True:
		first = int(e1*math.log(M) % math.log(n)) == int(math.log(c1))
		second = int(e2*math.log(M) % math.log(n)) == int(math.log(c2))
		if int(M)%1000 == 0:
			print e1*math.log(M) % math.log(n) , "    " , math.log(c1)
			print e2*math.log(M) % math.log(n)
			print "----------------"
		if first and second:
			print "ANSWER: " , M
			break

		M += 1

	return M



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


solve_rsa()
# solveTwomodularEquations(7, 2, 7, 6)