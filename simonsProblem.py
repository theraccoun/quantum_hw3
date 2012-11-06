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

	for col in range(len(mat[cur_row])):
		print "cur_matrix[",cur_row,'][',col,'] = ' , mat[cur_row][col]
		# raw_input()
		if mat[cur_row][col] == 1:
			for look_up in range(1, cur_row + 2):
				print "look_up: " , look_up
				if cur_row - look_up < 0:
					print "Searched all the way up!"
					return True
				if mat[cur_row-look_up][col] == 1:
					is_generate_new_row = True
					#look left to see if that row contains an earlier pivot
					if col != 0:
						for i in range(1, col+1):
							print "above and to da left: " , mat[cur_row-look_up][col-i] 
							# raw_input()
							if mat[cur_row-look_up][col-i] == 1:
								is_generate_new_row = False
								break

					if is_generate_new_row:
						new_row = []
						for c in range(len(mat[cur_row])):
							# print "cur_row: " , cur_row
							# print "c: " , c
							# print "mat[cur_row][c] " , mat[cur_row][c]
							# print "blah " , mat[cur_row-look_up][c]
							# print "XOR: " , mat[cur_row][c] , mat[cur_row-look_up][c]
							new_row.append(mat[cur_row][c] ^ mat[cur_row-look_up][c])
						mat[cur_row] = new_row
						print "NEW ROW: \n" , array(mat)
						break

	return False

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
		c = 0
		while not pivot_found:
			if my_array[r][c] == 1:
				print my_array[r][c]
				if r != c:
					temp = copy(my_array[c])
					my_array[c] = my_array[r]
					my_array[r] = temp

				pivot_found = True
			else:
				c += 1

	return my_array

def gaussian_elimination():
	mat = []
	s.connect((host, port));
	y = ""
	while len(mat) < 4:
		for i in range(4):
			y += str(randint(0,1))
		y = [int(bit) for bit in y]
		mat.append(y)
		#y = s.recv(1024).replace("\n", "")
		if is_linearly_independent(mat):
			print "IS LIN!!!!!"
		else:
			mat.pop()
			print "NOT LIN HAHAHAHH"
		y = ""

	print "FINAL ANS: \n" , array(mat)
	print make_lower_triangular(array(mat))


#mat = array([[0 for x in range(5)] for y in range(5)])
gaussian_elimination()



