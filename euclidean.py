#!/usr/bin/python

#Extended Euclid

def extended_euclid(u, v):
	u1 = 1
	u2 = 0
	u3 = u
	v1 = 0
	v2 = 1
	v3 = v
	while v3 != 0:
		q = u3 / v3
		t1 = u1 - q * v1
		t2 = u2 - q * v2
		t3 = u3 - q * v3
		u1 = v1
		u2 = v2
		u3 = v3
		v1 = t1
		v2 = t2
		v3 = t3

	return u1, u2

def common_modexp_attack(e1, e2, n, c1, c2):
	u, v = extended_euclid(e1, e2)
	print u,v
	M = (pow(c1,u, n) * pow(c2,v+n, n))%n
	print "M: \n" , M
	return M


e_1 = 65537
e_2 = 65539
c1 = 400030256839145194441034228199292487980894977737102147552044462667917219509871638663296814615652770720888715
c2 = 48384876797138828670281479166255073593234801358795810198774095180850824157124747742456773738763877257747936
n = 640434271860669796692811836922138143942513719203565769421924022297363333847089887235971007435680486193657059

common_modexp_attack(e_1, e_2, n, c1, c2)