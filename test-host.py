#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import httplib

dst = raw_input('input destination address :')

def ping(dst):
	try:
		os.system('ping -c 10 -I 192.168.122.1 {0}'.format(dst))
	except ValueError: print('Address error')
	try:
		os.system('ping -I 192.168.122.1 -ADb -c 10 -p ff -s 1452 -t 128 {0}'.format(dst))
	except ValueError: print('Address error')
	return

def trace(dst):
	try:
		print'-'*20
		print('ICMP traceroute')
		os.system('mtr -a 192.168.122.1 -tber {0}'.format(dst))
		print'-'*20
		print('TCP traceroute')
		os.system('mtr -a 192.168.122.1 -TP 80 -tber -B 255 {0}'.format(dst))
		print'-'*20
		print('UDP traceroute')
		os.system('mtr -a 192.168.122.1 -uP 53 -tber -B 255 {0}'.format(dst))
	except ValueError: print('Address error')
	return
	
def request(dst):
	try:
		get_rqst = ('HTTP request method GET to festination: ') + repr(dst)
		print(get_rqst)
		conn = httplib.HTTPConnection(dst)
		conn.request("GET","/")
		res = conn.getresponse()
		print res.status, res.reason
		conn.close()
		post_rqst = ('HTTP request method POST to festination: ') + repr(dst)
		print(post_rqst)
		conn = httplib.HTTPConnection(dst)
		conn.request("POST","/")
		res = conn.getresponse()
		print res.status, res.reason
		conn.close()
	except ValueError: print('Address error')
	return

ping(dst)
trace(dst)
print "-" * 60
request(dst)
print'='*60
print' '*60
print' '*60

# openssl connect to 443 port
tls_request = 'TLS request to destination: ' + repr(dst)
print(tls_request)
try:
	os.system('echo |openssl s_client -status -connect {0}:{1} {2} {3}'.format(dst,443,'|','tail'))
except ValueError: print('Address error')

print'='*60
print' '*60
print' '*60

# telnet to 80 port
tln_80 = 'Telnet connect to 80 port destination: ' + repr(dst)
print(tln_80)
try:
	os.system('telnet -b 192.168.122.1 {0} {1}'.format(dst,80))
except ValueError: print('Address error')

# telnet to 443 port
#tln_443 = 'Telnet connect to 443 port destination: ' + repr(dst)
#print(tln_443)
#try:
#	os.system('telnet -b 192.168.122.1 {0} {1}'.format(dst,443))
#except ValueError: print('Address error')
