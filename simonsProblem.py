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
	# print "--------------------------------------"
	# print "ar: \n" , array(mat)
	cur_row = len(mat) - 1

	for col in range(len(mat[cur_row])):
		# print "cur_matrix[",cur_row,'][',col,'] = ' , mat[cur_row][col]
		# raw_input()
		# print cur_row, mat[cur_row]
		if mat[cur_row][col] == 1:
			for look_up in range(1, cur_row + 2):

				examine_row_for_piv = cur_row-look_up
				if cur_row - look_up < 0:
					# print "cur_row=" , cur_row
					return True
				if mat[examine_row_for_piv][col] == 1:

					if row_contains_earlier_pivot(examine_row_for_piv, col, mat):
						new_row = []

						for c in range(len(mat[cur_row])):

							examine_row_value =  mat[examine_row_for_piv][c]
							cur_row_value = mat[cur_row][c]
							# print examine_row_value
							# print "c=" , c, " len=" , len(mat[cur_row])-1
							# raw_input()

							# if c == len(mat[cur_row])-1:
							# 	examine_row_value = int(examine_row_value.replace("|",""))
							# 	cur_row_value = int(cur_row_value.replace("|",""))
							# 	xored = cur_row_value ^ examine_row_value
							# 	print cur_row_value, examine_row_value, xored
							# 	print "examine: " , mat[examine_row_for_piv]
							# 	print "cur: " , mat[cur_row]
							# 	raw_input()
							# 	new_row.append("|" + str(xored))
							# 	print xored
							# 	print "NEW: " , new_row
							# else:
							# 	new_row.append(cur_row_value ^ examine_row_value)
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

	# for col in range(len(cur_matrix[cur_row])):
	# 	print "cur_matrix[",cur_row,'][',col,'] = ' , cur_matrix[cur_row][col]
	# 	raw_input()

	# 	if cur_matrix[cur_row][col] == 0:
	# 		print "0!"
	# 		continue
	# 	else:
	# 		print "meow"
	# for r in range(len(cur_matrix)):
	# 	for c in range(r+1):
	# 		print "cur_matrix[",r,'][',c,'] = ' , cur_matrix[r][c]
	# 		raw_input()

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

def get_all_linear_independents():
	mat_size = 4
	first_row = [0 for z in range(mat_size-1)]
	first_row.append(1)
	# first_row.append("|1")
	mat = [first_row]
	y = ""
	trials = 0
	while len(mat) < mat_size:
		for i in range(mat_size):
			y += str(randint(0,1))
		# s = socket.socket()
		# s.connect((host, port));
		# y = s.recv(2048).replace("\n", "")
		# s.close()
		y = y[:mat_size]
		y = [int(bit) for bit in y]
		if len(y) != mat_size:
			continue
		# y.append("|0")

		mat.append(y)
		# print len(mat)
		# print mat
		if not is_linearly_independent(mat):
			mat.pop()

		trials += 1
		# if trials%50 == 0:
		# 	print "TRIALS=" , trials

		y = ""

	# print "FINAL ANS: \n" , array(mat)
	# print "------------------------------------"
	# print "TRIALS: " , trials
	# print "LOWER TRIANG: \n" , make_lower_triangular(array(mat))

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
	for r in range(size(mat)-2):
		for col in range(r+1, m-1):
			if mat[r][col] == 1:
				xor_two_rows(r, col, mat)
				# print "NEW_MAT: \n" , mat
				# raw_input()
				# print "r+1=", r+1
				# for check_row in range(r+1, size(mat)):
				# 	# print col
				# 	# print mat[r]
				# 	# print mat[check_row]
				# 	raw_input()
				# 	if mat[check_row][col] == 1:
				# 		xor_two_rows(r, check_row, mat)
				# 		break

	print "second: \n" , mat

def add_b_vec(mat):
	mat[0].append(1)
	for r in range(1, len(mat)):
		mat[r].append(0)

amat = get_all_linear_independents()[0]
add_b_vec(amat)
print amat
amat = array(amat)
amat = make_lower_triangular(amat)


gaussian_elimination(amat)
#mat = array([[0 for x in range(5)] for y in range(5)])
# avg_trials = avg_lin_trials(3)
# print "AVG TRIALS: " , avg_trials



