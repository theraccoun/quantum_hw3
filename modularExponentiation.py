#Modular Exponentiation
import math

def modular_exponentiation(base, exponent, modulus):
	c = 1
	for e_prime in range(1, exponent+1):
		c = (c * base) % modulus
	return c

def successive_squaring(base, exponent, modulus):
	e = 1
	vals = {}
	while e <= exponent:
		sq = str(pow(base, e, modulus))
		vals[e] = sq
		e *= 2

	ex = exponent
	keys = sorted(vals)
	
	i = len(keys)-1
	total = 1
	while ex > 1:
		k = keys[i]
		i -= 1
		if ex - k < 0:
			continue
		else:
			total = (total*int(vals[k])) % modulus
			ex -= k

	return total



print "MINE: " , successive_squaring(1234, 1234*1234, int(math.pow(10,10)))
# print modular_exponentiation(1234, 1234*1234, math.pow(10, 10))
print "PYTH: " , pow(1234, 1234*1234, int(math.pow(10,10)))
