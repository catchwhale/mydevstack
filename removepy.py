#!/usr/bin/env python

import os
import sys

interface = sys.argv[1]
interface = interface.strip()
lst = ['ovs-vsctl del-port br-int ' + interface,
		'ip link delete dev ' + interface
		]
for i in lst:
	os.system(i)
