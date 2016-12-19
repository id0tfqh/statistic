#import sqlite3 as sql
#import sys

def data_path():
	try:
		date_parse = str(raw_input('date parsing in form of dd_mm : '))
	except(TypeError, ValueError):
		print ('Input is date in the form of dd_mm')
	data_path = '/home/bahu/.tolk/' + date_parse + '.db'
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
		dst_addr TEXT, type_request TEXT, request TEXT,\
		proto TEXT,	status INTEGER, body_size TEXT,\
		referer TEXT, user_agent TEXT);""")
	except sqlite.DatabaseError, err:
		print u"Error:", err
	else:
		print u"Question is comleted"
	conn.commit()
	conn.close()


def db_insert(data_path):
	import sqlite3 as sql
	conn = sql.connect(data_path)
	obj = conn.cursor()
	src_file = '///home/bahu/.tolk/rich-birds.com'
	content = open(src_file,"r",1)
	line = content.readline()
	for line in content.readlines():
		line = str(line)
		echo = line.split()[0]
		time_local = float(line.split()[1])
		http_host = line.split()[2]
		cache_status = line.split()[3]
		request_time = float(line.split()[4])
		src_addr = line.split()[5]
		dst_addr = line.split()[6]
		type_request = line.split()[10]
		request = line.split()[11]
		proto = line.split()[12]
		status = int(line.split()[13])
		body_size = line.split()[14]
		referer = line.split()[15]
		user_a = ' '.join(line.split()[16:])
		obj.execute("INSERT INTO parsing \
		(echo,time_local, http_host, cache_status, \
		request_time, src_addr, dst_addr, type_request, \
		request, proto, status, body_size, referer, user_agent) \
		VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
		(echo,time_local, http_host, cache_status, request_time, \
		src_addr, dst_addr, type_request, request, proto, status, \
		body_size, referer, user_a))
	conn.commit()
	conn.close()

	
data_path = '/home/bahu/.tolk/21_11.db'
import scipy
import sqlite3 as sql
conn = sql.connect(data_path)
obj = conn.cursor()
obj.execute("SELECT echo FROM parsing")
