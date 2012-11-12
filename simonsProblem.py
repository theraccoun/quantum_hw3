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

		trials += 1

		y = ""

	return [mat,trials]

def xor_two_rows(piv_row, second, mat):
	for i in range(len(mat[piv_row])):
		mat[piv_row][i] = mat[piv_row][i] ^ mat[second][i]

def avg_lin_trials(num_tries):
	avg_trial = 0
	for i in range(num_tries):
		print i
		avg_trial += get_all_linear_independents()

	return avg_trial/num_tries


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

def get_a(mat):
	ident = gaussian_elimination(mat)

	a = ""
	for r in range(len(ident)):
		a += str(ident[r][len(ident)])
	return a

def add_b_vec(mat):
	mat[0].append(1)
	for r in range(1, len(mat)):
		mat[r].append(0)

amat = get_all_linear_independents(128, True)[0]
print amat
add_b_vec(amat)
amat = array(amat)
make_lower_triangular(amat)


a = get_a(amat)
print "A=", a



