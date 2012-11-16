#Prime factorization

from random import randint
import math
import fractions
import modularExponentiation

n = 121932632103337941464563328643500519
print len(str(n))

def miller_rabin_pass(a, s, d, n):
	
	a_to_power = pow(a, d, n)
	if a_to_power == 1:
		return True
	for i in xrange(s-1):
		if a_to_power == n - 1:
			return True
		a_to_power = (a_to_power * a_to_power) % n
	return a_to_power == n - 1

def miller_rabin(n):
	#compute s and d
	d = n - 1
	s = 0
	while d % 2 == 0:
		d >>= 1
		s += 1

	#Run several miller_rabin passes
	for repeat in xrange(20):
		a = randint(2, n-1)
		if not miller_rabin_pass(a, s, d, n):
			return False
	return True

print miller_rabin(n)


def pollardRho(n):
	if n%2 == 0:
		return n

	x = randint(1, n-1)
	y = x
	c = randint(1, n-1)
	g = 1

	print "x: " , x
	print "c: " , c

	while g == 1:
		x = ((x*x)%n+c)%n
		y = ((y*y)%n+c)%n
		g = fractions.gcd(abs(x-y), n)

	return g

print "MILLER: " , miller_rabin(n)
# print "Pollard Rho: " , n , pollardRho(n)
