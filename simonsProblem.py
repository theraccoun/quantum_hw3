#!/usr/bin/python

import socket
import sys
from numpy import *
from random import randint

s = socket.socket()
host = "annai.cs.colorado.edu"
port = 443



def is_linearly_independent(mat, pivs_used):
	if len(mat) == 0:
		return True

	cur_row = len(mat) - 1

	for col in range(len(mat[cur_row])-1):
		if mat[cur_row][col] == 1:
			for look_up in range(1, cur_row + 2):

				examine_row_for_piv = cur_row-look_up
				if cur_row - look_up < 0:
					pivs_used.remove(col)
					return True
				if mat[examine_row_for_piv][col] == 1:

					if row_contains_earlier_pivot(examine_row_for_piv, col, mat):
						# print "BEFORE: \n" , array(mat)
						# print cur_row, examine_row_for_piv
						xor_two_rows(cur_row, examine_row_for_piv, mat)
						# print "AFTER: \n" , array(mat)
						# raw_input()
						# new_row = []

						# for c in range(len(mat[cur_row])):

						# 	examine_row_value =  mat[examine_row_for_piv][c]
						# 	cur_row_value = mat[cur_row][c]
						# 	new_row.append(cur_row_value ^ examine_row_value)


						# mat[cur_row] = new_row
						break

	return False

#look left to see if that row contains an earlier pivot
def row_contains_earlier_pivot(examine_row, col, mat):
	if col != 0:
		for i in range(1, col+1):
			if mat[examine_row][col-i] == 1:
				return False
	return True

def make_lower_triangular(my_array):
	r = 0
	while r < len(my_array):

		pivot_found = False
		for c in range(len(my_array[r])-1):
			if int(my_array[r][c]) == 1:
				if r != c:
					print r,c
					temp = copy(my_array[c])
					my_array[c] = my_array[r]
					my_array[r] = temp
				else:
					r += 1

				break

	return my_array

# def get_random_a(init_y):
# 	a = ""
# 	initial_y = ""
# 	for i in range(len(init_y)-1):
# 		initial_y += str(init_y[i])

# 	while True:
# 		for i in range(len(initial_y)):
# 			a += str(randint(0,1))

# 		print a, initial_y
# 		a_dot_y = dot_prod_of_binary_vectors(a, initial_y)
# 		if a_dot_y == 1:
# 			break
# 		else:
# 			a = "" 
	
# 	print "A=" , a
# 	return a

def get_random_a(size):
	a = ""
	for i in range(size):
		a += str(randint(0,1))

	print "ORIG A: " , a
	return a

def get_all_linear_independents(mat_size, from_server):
		
	# first_row = [0 for z in range(mat_size-1)]
	# first_row.append(1)
	# first_row.append(1)
	if not from_server:
		a = get_random_a(mat_size)

	# original = [[f for f in first_row]]
	# mat = [first_row]
	original = []
	mat = []
	pivs_used = [p for p in range(mat_size)]
	y = ""
	trials = 0
	while len(pivs_used) > 1:
		if not from_server:
			while True:
				for i in range(mat_size):
					y += str(randint(0,1))

				a_dot_y = dot_prod_of_binary_vectors(a, y)
				if a_dot_y == 0:
					break
				else:
					y = ""
		else:
			s = socket.socket()
			s.connect((host, port));
			y = s.recv(2048).replace("\n", "")
			s.close()
		y = y[:mat_size]
		y = [int(bit) for bit in y]
		y.append(0)
		# print "mat: \n" , array(mat)

		mat.append(y)
		
		if not is_linearly_independent(mat, pivs_used):
			mat.pop()
		else:
			original.append(y)

		trials += 1
		y = []

	print "bef ins: \n" , mat
	insert_last_row(mat, pivs_used[0], original)
	print "pos: \n" , mat
	return [mat,trials, original]

def insert_last_row(mat, last_piv, original):
	print last_piv
	last_row = []
	for c in range(len(mat[0])):
		if c == last_piv or c == len(mat[0])-1:
			last_row.append(1)
		else:
			last_row.append(0)

	mat.append(last_row)
	original.append(last_row)
	return

def xor_two_rows(piv_row, second, mat):
	for i in range(len(mat[piv_row])):
		mat[piv_row][i] = mat[piv_row][i] ^ mat[second][i]

def avg_lin_trials(num_tries):
	avg_trial = 0
	for i in range(num_tries):
		print i
		avg_trial += get_all_linear_independents()

	return avg_trial/num_tries

def dot_prod_of_binary_vectors(a, b):
	if len(a) != len(b): return

	dot = int(a[0]) and int(b[0])

	for i in range(1, len(a)):
		dot ^= int(a[i]) and int(b[i])

	return dot

def gaussian_elimination(mat):
	print "first: \n" , mat
	m = len(mat[0])
	a = ""
	for r in range(size(mat)-2):
		for col in range(r+1, m-1):
			if mat[r][col] == 1:
				xor_two_rows(r, col, mat)

	print "second: \n" , mat
	return mat

def solve_for_a(mat):
	ident = gaussian_elimination(mat)

	a = ""
	for r in range(len(ident)):
		a += str(ident[r][len(ident)])
	return a

def add_b_vec(mat):
	mat[0].append(1)
	for r in range(1, len(mat)):
		mat[r].append(0)

def get_string_value(s):
	val = 0
	for i in range(len(s)):
		val += pow(2,i)

	return val

def test_mat(a, original):
	for r in range(len(original)):
		test = original[r]
		test_str = ""
		for c in range(len(test)-1):
			test_str += str(original[r][c])


		dot_with_a = dot_prod_of_binary_vectors(a, test_str)

		if dot_with_a != 0:
			print "BAD VECTOR!"
			print "row: " , r
			print a
			print test_str

meta_lins = get_all_linear_independents(128, True)
amat = meta_lins[0]
trials = meta_lins[1]
original = meta_lins[2]
# print amat
# add_b_vec(amat)
amat = array(amat)
print amat
make_lower_triangular(amat)

a = solve_for_a(amat)
original = array(original)
# print "original: \n" , array(original)
make_lower_triangular(original)
print "original: \n" , array(original)
print "A=" , a
print "A=", get_string_value(a)
raw_input()
test_mat(a, original)




