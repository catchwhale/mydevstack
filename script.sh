#path to impl_vsctl.py
rm -r /opt/stack/neutron/neutron/agent/ovsdb/impl_vsctl.py
cp impl_vsctl.py /opt/stack/neutron/neutron/agent/ovsdb/

#path to commands.py
rm -r /opt/stack/neutron/neutron/agent/ovsdb/native/commands.py
cp commands.py /opt/stack/neutron/neutron/agent/ovsdb/native 

#path to interface.py
rm -r /opt/stack/neutron/neutron/agent/linux/interface.py
cp interface.py /opt/stack/neutron/neutron/agent/linux/

#path to ovs_lib.py
rm -r /opt/stack/neutron/neutron/agent/linux/interface.py
cp interface.py /opt/stack/neutron/neutron/agent/linux/