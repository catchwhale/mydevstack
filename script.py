#!/usr/bin/env python
#path to impl_vsctl.py
import os

# os.system('cp /opt/stack/neutron/neutron/agent/linux/ip_link_support.py /opt/stack/neutron/neutron/agent/linux/ip_link_support_orig.py')
# os.system('cp /opt/stack/neutron/neutron/agent/linux/interface.py /opt/stack/neutron/neutron/agent/linux/interface_orig.py')

lst = [ '/opt/stack/neutron/neutron/agent/ovsdb/impl_vsctl.py',
		'/opt/stack/neutron/neutron/agent/linux/ip_link_support.py',
		'/opt/stack/neutron/neutron/agent/linux/interface.py'
		# '/opt/stack/neutron/neutron/agent/ovsdb/impl_vsctl.py', \
		# '/opt/stack/neutron/neutron/agent/ovsdb/native/commands.py', \
		# '/opt/stack/neutron/neutron/agent/linux/interface.py', \
		# '/usr/bin/modify', \
		# '/opt/stack/neutron/neutron/agent/ovsdb/api.py', \
		# '/opt/stack/neutron/neutron/agent/ovsdb/impl_idl.py'
	]
for i in lst:
	py = i.split('/')
	py = py[-1]
	if os.path.isfile(i):
		print i, ' = Exists!'
		os.system('rm -r ' + i)
		if not os.path.isfile(i):
			print i, ' Successfully removed!'

	else:
		print i, ' =  Does not exists!'
	os.system('cp ' + py + ' ' + i)
	if os.path.isfile(i):
		print i, ' Successfully added!'
	else:
		print i, ' Failure to add!'

dir_ = os.popen('echo $HOME').read()
dir_ = dir_.strip() + '/devstack'
os.chdir(dir_)
os.system('./unstack.sh')
os.system('./stack.sh')


# impl_vsctl = '/opt/stack/neutron/neutron/agent/ovsdb/impl_vsctl.py'
# if os.path.isfile(impl_vsctl):
# 	os.system('rm -r ' + impl_vsctl)
# 	os.system('cp impl_vsctl.py /opt/stack/neutron/neutron/agent/ovsdb')

# #path to commands.py
# commands = '/opt/stack/neutron/neutron/agent/ovsdb/native/commands.py'
# if os.path.isfile(commands):
# 	os.system('rm -r ' + commands)
# 	os.system('cp commands.py /opt/stack/neutron/neutron/agent/ovsdb/native') 

# #path to interface.py
# interface = '/opt/stack/neutron/neutron/agent/linux/interface.py'
# if os.path.isfile(interface):
# 	os.system('rm -r ' + interface)
# 	os.system('cp interface.py ' + interface)

#path to ovs_lib.py

# if os.path.isfile():
# rm -r /opt/stack/neutron/neutron/agent/linux/interface.py
# cp interface.py /opt/stack/neutron/neutron/agent/linux

# modify = '/usr/bin/modify'
# if os.path.isfile(modify):
# 	os.system('rm -r ' + modify)
# 	os.system('cp modify /usr/bin')

# api = '/opt/stack/neutron/neutron/agent/ovsdb/api.py'
# if os.path.isfile(api):
# 	os.system('rm -r ' + api)
# 	os.system('cp api.py ' + api)

# impl_idl = '/opt/stack/neutron/neutron/agent/ovsdb/impl_idl.py'
# if os.path.isfile(impl_idl):
# 	os.system('rm -r ' + impl_idl)
# 	os.system('cp impl_idl.py ' + impl_idl)







