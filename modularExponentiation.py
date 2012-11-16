#Modular Exponentiation
import math

def modular_exponentiation(base, exponent, modulus):
	c = 1
	for e_prime in range(1, exponent+1):
		c = (c * base) % modulus
	return c

def successive_squaring(base, exponent, modulus):
	print exponent
	e = 1
	vals = {}
	while e <= exponent:
		sq = str(pow(base, e, modulus))
		vals[e] = sq
		print base , "^" , e, "    " , sq
		e *= 2

	print vals

	ex = exponent
	keys = sorted(vals)
	print keys
	
	i = len(keys)-2
	total = int(vals[keys[i]])
	while ex > 1:
		k = keys[i]
		i -= 1
		print "ex: " , ex
		if ex - k < 0:
			continue
		else:
			total = (total*int(vals[k])) % modulus
			print "GOOD: " , ex
			ex -= k

	print total
		# i = 0
		# k = 0
		# while i < len(keys):
		# 	k = keys[i]
		# 	if k > ex:
		# 		k = keys[i-1]
		# 		break
		# 	i += 1

		# print "ex: " , ex
		# ex -= k
		# if ex in keys:
		# 	print ex
		# 	total *= keys[ex]
		# i += 1



successive_squaring(1234, 1234*1234, int(math.pow(10,10)))
# print modular_exponentiation(1234, 1234*1234, math.pow(10, 10))
print pow(1234, 1234*1234, int(math.pow(10,10)))
