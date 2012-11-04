#!/usr/bin/python

import socket
import sys

# s = socket.socket()
host = "annai.cs.colorado.edu"
port = 443

def is_linearly_independent(bin_string, valid_strings):
	print "lenval: " , len(valid_strings)
	if len(valid_strings) == 0: return True

	# xored_strings = bin_string

	# for li_string in valid_strings:

	# 	for c in range(len(li_string)):
	# 		if int(li_string[i]) ^ int(xored_strings[i] == 1:
	# 			break

	# 	if xored_strings == 0:
	# 		return False
		
	# return True

	for i in range(len(bin_string)):

		xor_at_col = int(bin_string[i])

		for li in valid_strings:
			xor_at_col ^= int(li[i])

		if xor_at_col > 0:
			return True

	return False

def is_linearly_independent(s1, s2):
	if len(s1) != len(s2):
		print "lengths must match"
		sys.exit()

	for i in range(len(s1)):
		if s1[i] != s2[i]:
			return True

	return False


def get_all_linearly_indp_strings():
	lin_indep_strings = []

	for i in range(20):
		s = socket.socket()
		s.connect((host, port))
		bstrn_from_server = s.recv(1024).replace("\n", "")

		if len(bstrn_from_server) != 128: continue	 

		print "meow: " , bstrn_from_server
		print "lin_ind_list: " , lin_indep_strings

		if is_linearly_independent(bstrn_from_server, lin_indep_strings):
			lin_indep_strings.append(bstrn_from_server)

		s.close()

print "IS_LIN? " , is_linearly_independent("11101", "10101")
# get_all_linearly_indp_strings()



