#path to impl_vsctl.py
rm -r /opt/stack/neutron/neutron/agent/ovsdb/impl_vsctl.py
cp impl_vsctl.py /opt/stack/neutron/neutron/agent/ovsdb

#path to commands.py
rm -r /opt/stack/neutron/neutron/agent/ovsdb/native/commands.py
cp commands.py /opt/stack/neutron/neutron/agent/ovsdb/native 

#path to interface.py
rm -r /opt/stack/neutron/neutron/agent/linux/interface.py
cp interface.py /opt/stack/neutron/neutron/agent/linux

#path to ovs_lib.py
rm -r /opt/stack/neutron/neutron/agent/linux/interface.py
cp interface.py /opt/stack/neutron/neutron/agent/linux

rm -r /usr/bin/modify
cp modify /usr/bin

rm -r /opt/stack/neutron/neutron/agent/ovsdb/api.py
cp api.py /opt/stack/neutron/neutron/agent/ovsdb

rm -r /opt/stack/neutron/neutron/agent/ovsdb/impl_idl.py
cp impl_idl.py /opt/stack/neutron/neutron/agent/ovsdb







