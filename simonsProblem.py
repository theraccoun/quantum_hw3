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
	print "--------------------------------------"
	print array(mat)
	cur_row = len(mat) - 1

	for col in range(len(mat[cur_row])-1):
		print "cur_matrix[",cur_row,'][',col,'] = ' , mat[cur_row][col]
		# raw_input()
		if mat[cur_row][col] == 1:
			for look_up in range(1, cur_row + 2):
				print "look_up: " , look_up
				examine_row_for_piv = cur_row-look_up
				if cur_row - look_up < 0:
					print "Searched all the way up!"
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

							if c == len(mat[cur_row])-1:
								examine_row_value = int(examine_row_value.replace("|",""))
								cur_row_value = int(cur_row_value.replace("|",""))
								xored = cur_row_value ^ examine_row_value
								new_row.append("|" + str(xored))
							else:
								new_row.append(cur_row_value ^ examine_row_value)

						mat[cur_row] = new_row
						print "NEW ROW: \n" , array(mat)
						break

	return False

#look left to see if that row contains an earlier pivot
def row_contains_earlier_pivot(examine_row, col, mat):
	if col != 0:
		for i in range(1, col+1):
			print "above and to da left: " , mat[examine_row][col-i] 
			# raw_input()
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

def gaussian_elimination():
	mat = []
	mat_size = 4
	s.connect((host, port));
	y = ""
	while len(mat) < mat_size:
		for i in range(mat_size):
			y += str(randint(0,1))
		y = [int(bit) for bit in y]
		y.append("|0")
		mat.append(y)
		#y = s.recv(1024).replace("\n", "")
		if is_linearly_independent(mat):
			print "IS LIN!!!!!"
		else:
			mat.pop()
			print "NOT LIN HAHAHAHH"
		y = ""

	print "FINAL ANS: \n" , array(mat)
	print "LOWER TRIANG: \n" , make_lower_triangular(array(mat))


#mat = array([[0 for x in range(5)] for y in range(5)])
gaussian_elimination()



