#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os
import re

pattern = r'^[0-9.]+$'
try:
	addr = raw_input('input ip address: \n')
	if re.match(pattern, addr):
		pass
	else: 
		print('A incorrect address')
		addr = '192.168.1.1'
except ValueError: print "A incorrect address"

command = 'ipset -L | grep '
command = command + addr

os.system('ssh -24xCt tech@base221 sudo {0}'.format(command))
os.system('ssh -24xCt tech@base222 sudo {0}'.format(command))
os.system('ssh -24xCt tech@base241 sudo {0}'.format(command))
