#Modular Exponentiation
import math

def modular_exponentiation(base, exponent, modulus):
	c = 1
	for e_prime in range(1, exponent+1):
		c = (c * base) % modulus
	return c

print modular_exponentiation(1234, 1234*1234, math.pow(10, 10))
print pow(1234, 1234*1234, int(math.pow(10,10)))
