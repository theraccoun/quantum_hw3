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
	# print array(mat)
	cur_row = len(mat) - 1

	for col in range(len(mat[cur_row])):
		# print "cur_matrix[",cur_row,'][',col,'] = ' , mat[cur_row][col]
		# raw_input()
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
							# 	new_row.append("|" + str(xored))
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
	mat = []
	mat_size = 128
	y = ""
	trials = 0
	while len(mat) < mat_size:
		for i in range(mat_size):
			y += str(randint(0,1))
		# s = socket.socket()
		# s.connect((host, port));
		# y = s.recv(2048).replace("\n", "")
		# s.close()
		# y = y[:mat_size]
		y = [int(bit) for bit in y]
		
		if len(y) != mat_size:
			continue
		# y.append("|0")

		mat.append(y)
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

	return trials

def avg_lin_trials(num_tries):
	avg_trial = 0
	for i in range(num_tries):
		print i
		avg_trial += get_all_linear_independents()

	return avg_trial/num_tries



#mat = array([[0 for x in range(5)] for y in range(5)])
avg_trials = avg_lin_trials(100)
print "AVG TRIALS: " , avg_trials



