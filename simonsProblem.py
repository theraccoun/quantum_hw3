#!/usr/bin/python

import socket
import sys
from numpy import *
from random import randint

s = socket.socket()
host = "annai.cs.colorado.edu"
port = 443



def is_linearly_independent(mat):
	if len(mat) == 0:
		return True

	cur_row = len(mat) - 1

	for col in range(len(mat[cur_row])):
		if mat[cur_row][col] == 1:
			for look_up in range(1, cur_row + 2):

				examine_row_for_piv = cur_row-look_up
				if cur_row - look_up < 0:
					return True
				if mat[examine_row_for_piv][col] == 1:

					if row_contains_earlier_pivot(examine_row_for_piv, col, mat):
						new_row = []

						for c in range(len(mat[cur_row])):

							examine_row_value =  mat[examine_row_for_piv][c]
							cur_row_value = mat[cur_row][c]
							new_row.append(cur_row_value ^ examine_row_value)


						mat[cur_row] = new_row
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
	for r in range(len(my_array)):

		pivot_found = False
		for c in range(len(my_array[r])-1):
			if int(my_array[r][c]) == 1:
				if r != c:
					temp = copy(my_array[c])
					my_array[c] = my_array[r]
					my_array[r] = temp

				break
			else:
				c += 1

	return my_array

def get_all_linear_independents(mat_size, from_server):
	first_row = [0 for z in range(mat_size-1)]
	original = [[f for f in first_row]]
	first_row.append(1)
	mat = [first_row]
	y = ""
	trials = 0
	while len(mat) < mat_size:
		if not from_server:
			for i in range(mat_size):
				y += str(randint(0,1))
		else:
			s = socket.socket()
			s.connect((host, port));
			y = s.recv(2048).replace("\n", "")
			s.close()
		y = y[:mat_size]
		y = [int(bit) for bit in y]
		if len(y) != mat_size:
			continue

		mat.append(y)
		
		if not is_linearly_independent(mat):
			mat.pop()
		else:
			original.append(y)

		trials += 1

		y = ""

	return [mat,trials, original]

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

def test_mat(a, original):
	for r in range(len(original)):
		test = original[r]
		test_str = ""
		for c in range(len(test)):
			test_str += str(original[r][c])

		print "a: " , a
		print len(a)
		print "test_str: " , test_str
		print len(test_str)
		raw_input()

		dot_with_a = dot_prod_of_binary_vectors(a, test_str)

		if dot_with_a != 0:
			print "BAD VECTOR!"
			print "row: " , r
			print dot_with_a

meta_lins = get_all_linear_independents(4, False)
amat = meta_lins[0]
trials = meta_lins[1]
original = meta_lins[2]
print amat
add_b_vec(amat)
amat = array(amat)
make_lower_triangular(amat)

a = solve_for_a(amat)
print "A=", a
raw_input()
test_mat(a, original)




