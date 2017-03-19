#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as sql
# Istall external standart encoding of utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import logging
import re

LOG_FILE = '///opt/pyt/error_file'
SRC_FILE = '///home/bahu/rirds'

log_level = logging.WARNING
log_format = '%(asctime)s | line:%(lineno)d | %(levelname)-8s: %(message)s'
logging.basicConfig(level=log_level, format=log_format, filename=LOG_FILE, filemode='w')

def data_path():
	try:
		date_parse = str(raw_input('date parsing in form of dd_mm : '))
	except(TypeError, ValueError):
		print ('Input is date in the form of dd_mm')
	data_path = '/home/bahu' + date_parse + '.db'
	return data_path

def db_create(data_path):
	import sqlite3 as sql
	conn = sql.connect(data_path)
	obj = conn.cursor()
	try:
		obj.executescript("""
		CREATE TABLE IF NOT EXISTS parsing\
		(echo TEXT, time_local REAL, http_host TEXT,\
		cache_status TEXT, request_time REAL, src_addr TEXT,\
		dst_addr TEXT, type_request TEXT, request BINARY,\
		proto TEXT, status INTEGER, body_size TEXT,\
		referer TEXT, user_agent TEXT, row_string TXT);""")
	except sqlite.DatabaseError, err:
		print u"Error:", err
	else:
		print u"Question is comleted"
	conn.commit()
	conn.close()


def db_insert(data_path):
	pattern_request = 'HTTP/..."$'
	compile_re = re.compile(pattern_request)
	def quest(ln):
		if compile_re.search(' '.join(ln[11:15])) is None: pass
		else: quest = ' '.join(ln[11:14])
		if compile_re.search(' '.join(ln[11:14])) is None: pass
		else: quest = ' '.join(ln[11:13])
		if compile_re.search(' '.join(ln[11:13])) is None: pass
		else: quest = ' '.join(ln[11:12])
		if compile_re.search(' '.join(ln[11:12])) is None: pass
		else: quest = ln[11]
		return quest
	conn = sql.connect(data_path)
	obj = conn.cursor()
	with open(SRC_FILE,'r',1) as content:
		for line in content:
			line = str(line) # с ковычками может быть невыносимо как жутко в запросе
			ln = line.decode('utf8').split()
			echo = ln[0]
			time_local = float(ln[1])
			http_host = ln[2]
			cache_status = ln[3]
			request_time = float(ln[4])
			src_addr = ln[5]
			dst_addr = ln[6]
			type_request = ln[10]
			request = quest(ln)
			#request = ln[11] # попробовать писать в базу в бинарном формате
			proto = ln[12]
			status = int(ln[13])
			body_size = ln[14]
			referer = ln[15]
			user_a = ' '.join(ln[16:])
			try:
				obj.execute("INSERT INTO parsing\
				(echo,time_local, http_host, cache_status,\
				request_time, src_addr, dst_addr, type_request,\
				request, proto, status, body_size, referer, user_agent)\
				VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",\
				(echo,time_local, http_host, cache_status, request_time,\
			 	src_addr, dst_addr, type_request, request, proto, status,\
			 	body_size, referer, user_a))
			except (UnicodeEncodeError, ValueError):
				obj.execute("INSERT INTO parsing\
				(echo, time_local, http_host, cache_status,\
				request_time, src_addr, dst_addr, type_request,\
				row_string)VALUES (?,?,?,?,?,?,?,?,?)",\
				(echo,time_local, http_host, cache_status, request_time,\
				src_addr, dst_addr, type_request, row_string))
			finally:
				pass
				#print
	conn.commit()
	conn.close()
	#err_content.close()
	

	
data_path = '/home/bahu/21_11.db'
import scipy
import sqlite3 as sql
conn = sql.connect(data_path)
obj = conn.cursor()
obj.execute("SELECT echo FROM parsing")
while echo is not None:
     echo = obj.fetchone()[0]
    

obj.execute("SELECT DISTINCT time_local FROM parsing")
while time_local is not None:
    time_local = obj.fetchone()[0]
  
    
obj.execute("SELECT DISTINCT user_agent FROM parsing")
user_agent = obj.fetchone()[0]


conn.commit()
conn.close()
