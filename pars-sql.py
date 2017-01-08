import sqlite3 as sql
# Istall external standart encoding of utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import logging

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
		dst_addr TEXT, type_request TEXT, request TEXT,\
		proto TEXT, status INTEGER, body_size TEXT,\
		referer TEXT, user_agent TEXT);""")
	except sqlite.DatabaseError, err:
		print u"Error:", err
	else:
		print u"Question is comleted"
	conn.commit()
	conn.close()


def db_insert(data_path):
	conn = sql.connect(data_path)
	obj = conn.cursor()
	with open(SRC_FILE,'rt',1) as content:
		for line in content.readlines():
			#line =line.strip
			ln = line.decode('utf8').split
			echo = ln[0]
			time_local = float(ln[1])
			http_host = ln[2]
			cache_status = ln[3]
			request_time = float(ln[4])
			src_addr = ln[5]
			dst_addr = ln[6]
			type_request = ln[10]
			request = ln[11]
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
			except (UnicodeEncodeError, ValueError) as err:
				logging.WARNING(line)
				# logging.WARNING('{}: {}'.format(err, line))
			except:
				logging.ERROR(sys.exc_info())
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
