#!/usr/bin/env python
#path to impl_vsctl.py
import os

# os.system('cp /opt/stack/neutron/neutron/agent/linux/ip_link_support.py /opt/stack/neutron/neutron/agent/linux/ip_link_support_orig.py')
# os.system('cp /opt/stack/neutron/neutron/agent/linux/interface.py /opt/stack/neutron/neutron/agent/linux/interface_orig.py')
# os.system('cp modify /usr/bin/0')
# os.system('chmod +x /usr/bin/modify')

lst = [ '/opt/stack/neutron/neutron/agent/ovsdb/impl_vsctl.py',
		'/usr/bin/modify',
		'/opt/stack/neutron/neutron/agent/ovsdb/ovs_vsctl_enhance.py'
		# '/opt/stack/neutron/neutron/agent/linux/ip_link_support.py',
		# '/opt/stack/neutron/neutron/agent/linux/interface.py'
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
os.system('ln /usr/bin/modify /usr/bin/0')
if os.path.isfile('/usr/bin/modify'):
	os.system('chmod +x /usr/bin/modify')
	print 'modification successfully updated.'
dir_ = os.popen('echo $HOME').read()
dir_ = dir_.strip() + '/devstack'
os.chdir(dir_)
print 'Preparing to uninstall stack...'
os.system('./unstack.sh')
print 'Preparing to install stack...'
os.system('./stack.sh')



