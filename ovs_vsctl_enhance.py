#!/usr/bin/env python
"""
The purpose of the program is test if interface given can communicate using TAP to an existing bridge
If interface is invalid then will be displayed an error and then will not be added in  bridge
"""

import os
import fcntl
import struct
import re
import subprocess

def remov_element(my_list, key_val):
	try:
		my_list.remove(key_val) #del key_value tag 
	except:
		pass
	return my_list

# Get all bridges with their interfaces
def get_all_bridges_w_interfaces():
	br = os.popen('ovs-vsctl show').readlines() # CLI command to get all bridges
	# Initialize all List variables
	invalid_intF = []
	cnt_Br = 0
	myIntF = []
	all_Bridges = []
	all_myIntF = []
	intF_typ = []
	add_intF = []
	for i in br:
		i = i.strip()
		if re.search('Bridge', i): # if bridge is detected
			cnt_Br += 1 # increment
			bridge = i.split() # split into white space
			bridge = bridge[-1] # get the last element at index N
			bridge = bridge.replace('"', '') # replace '"' with empty
			#print bridge
			all_Bridges.append(bridge) # add new bridge
		elif re.search('Interface', i) or re.search('type', i) or re.search('tag', i): # search if Interface, type or tag is found
			if not re.search('tag', i): #if not tag was found
				i = i.split() # split into space
				i = i[1] # get the at the 2nd index
				i = i.replace('"', '') # replace '"' with empty
				intF_typ.append(i) # add interface 
				myIntF.append(i) # add interface
			else:
				intF_typ.append('tag') # add tag
				myIntF.append('tag') # add tag
		if re.search('Port', i) and len(intF_typ) > 0: # if Port string is found and intF_typ is greater than 0
			if len(intF_typ) == 2 or len(intF_typ) == 3: # Len is between 2 to 3
				intF_typ = remov_element(intF_typ, 'tag') #delete key value tag 
				add_intF += intF_typ # add new interface
			else:
				invalid_intF.append(intF_typ[0]) # add new invalid interface at index 0
				print 'invalid interface: ',intF_typ[0]
				if intF_typ[0]:
					try:
						#pass
						for c in all_Bridges:
							#pass
							remove_interface(intF_typ[0], c)
					except: pass
			intF_typ = [] # Restore to empty list
		if cnt_Br > 0 and re.search('Bridge', i): # count is greater than 0 and Bridge string is found
			if len(myIntF) > 0: # if greater than 0
				all_myIntF.append(add_intF) # add new interface
				add_intF = [] # initial back to empty
	all_myIntF.append(add_intF) # add the last index of add_intF interface
	intF_typ = remov_element(intF_typ, 'tag') #delete key value tag at List "intF_typ" 
	all_myIntF.append(intF_typ) # adding new interface type: internal
# Remove interface
def remove_interface(interface, bridge):
	lst = [('sudo ovs-vsctl clear Bridge ' + bridge + ' mirrors'),
			('sudo ovs-vsctl del-port ' + bridge + ' ' + interface),
			('sudo ip link delete dev ' + interface)
		]
	for i in lst:
		try:
			os.system(i)
		except:
			pass





