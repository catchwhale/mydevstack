#!/usr/bin/env python

import os
import sys

input = sys.argv[1]
input = input.strip()
os.system('ip link add name ' + input ' type dummy')
os.system('ip link set dev ' + input + ' up')
os.system('ovs-vsctl add-port br-int ' + input)