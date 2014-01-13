#-*- coding: utf-8 -*-
'''
	Python Standard Library
	See Also: http://docs.python.org/3/library/index.html
'''
import threading, time
'''
	Thread-based parallelism
	See Also: http://docs.python.org/3/library/threading.html
'''

def func(arg):
	time.sleep(1)
	print('thread: ' + str(arg))


for i in range(5):
	t = threading.Thread(None, func, args=(i,))
	t.start()

import logging, os, sys, logging.config
'''
	Logging facility for Python
	See Also: http://docs.python.org/3/library/logging.html
'''
# basicConfig
if os.name == 'nt':
	# logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
	logging_file = 'c:/test.log'
elif os.name == 'posix':
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')
logging.basicConfig(
    level=logging.DEBUG,
    filename = logging_file,
    filemode = 'a+',
	format='%(asctime)s [%(name)s] [%(levelname)s] [%(filename)s:%(lineno)s] - %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S'
)
logging.debug("debug log")
logging.info("info log")
logging.warning("warning log")
logging.error("error log")
logging.fatal("fatal log")
logging.critical("critical log")
try:
	raise NameError('name error')
except:
	logging.exception("exception log")

# fileConfig
curpath = os.path.dirname(sys.argv[0])
os.chdir(curpath)
LOG_CONFIG = 'logging.conf'
logging.config.fileConfig(LOG_CONFIG)
logger = logging.getLogger("standardlibrary")
logger.debug("debug log")
logger.info("info log")
logger.warning("warning log")
logger.error("error log")
logger.fatal("fatal log")
logger.critical("critical log")
try:
	raise NameError('name error')
except:
	logger.exception("exception log")
logging.debug("debug log")
logging.info("info log")
logging.warning("warning log")
logging.error("error log")
logging.fatal("fatal log")
logging.critical("critical log")
try:
	raise NameError('name error')
except:
	logging.exception("exception log")


logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)
# StreamHandler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
# FileHandler
ch = logging.FileHandler('c:/test1.log', 'a+', encoding='utf-8')
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)
# NullHandler
# WatchedFileHandler
# BaseRotatingHandler
# RotatingFileHandler
# TimedRotatingFileHandler
# SocketHandler
# DatagramHandler
# SysLogHandler
# NTEventLogHandler
# SMTPHandler
# MemoryHandler
# HTTPHandler
# QueueHandler
'''
	Logging handlers
	See Also: http://docs.python.org/3/library/logging.handlers.html
'''

logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")


import sqlite3
'''
	DB-API 2.0 interface for SQLite databases
	See Also: http://docs.python.org/3/library/sqlite3.html
'''
conn = sqlite3.connect('c:/test.db')
csr = conn.cursor()
csr.execute("""DROP TABLE IF EXISTS [user]""")
csr.execute("""
CREATE TABLE IF NOT EXISTS [user] (
  [id] NUMBER NOT NULL, 
  [name] TEXT NOT NULL, 
  CONSTRAINT [] PRIMARY KEY ([id]));
""")
csr.execute("insert into user(id,name) values (1, 'a')")
csr.execute("insert into user(id,name) values (2, 'b')")
csr.execute("insert into user(id,name) values (3, 'c')")
conn.commit()

csr.execute('SELECT id, name from user where id > 1')
data = csr.fetchone()
while data:
	for d in data:
		print(d)
	data = csr.fetchone()

print('*'*80)

csr.execute('SELECT id, name from user where id > 1')
data = csr.fetchall()
for r in data:
	for c in r:
		print(c)

conn.close()


import urllib.request, urllib.parse, http.cookiejar

print(urllib.request.urlopen('http://www.baidu.com/').read().decode())

urllib.request.urlretrieve('http://su.bdimg.com/static/superpage/img/logo.png', 'c:/logo.png')

req = urllib.request.Request('http://www.baidu.com/')

req.headers = {
	'Host': 'www.baidu.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
}

req.add_header('Referer', 'http://www.baidu.com/')

print(urllib.request.urlopen(req).read().decode())

print(urllib.parse.quote('!@#$%^&*()_+')) # %21%40%23%24%25%5E%26%2A%28%29_%2B
print(urllib.parse.unquote('%21%40%23%24%25%5E%26%2A%28%29_%2B')) # !@#$%^&*()_+

print(urllib.parse.splitattr('http://www.baidu.com/;attr=value')) # ('http://www.baidu.com/', ['attr=value'])
print(urllib.parse.splithost('//www.baidu.com/index.html')) # ('www.baidu.com', '/index.html')
print(urllib.parse.splitnport('www.baidu.com:8080', 80)) # ('www.baidu.com', 8080)
print(urllib.parse.splitpasswd('rileyren:123456')) # ('rileyren', '123456')
print(urllib.parse.splitport('www.baidu.com:8080')) # ('www.baidu.com', '8080')
print(urllib.parse.splitquery('http://www.baidu.com/index.html?id=1')) # ('http://www.baidu.com/index.html', 'id=1')
print(urllib.parse.splittag('http://www.baidu.com/index.html?id=1#tag1')) # ('http://www.baidu.com/index.html?id=1', 'tag1')
print(urllib.parse.splittype('http://www.baidu.com/index.html')) # ('http', '//www.baidu.com/index.html')
print(urllib.parse.splituser('rileyren:123456@www.baidu.com')) # ('rileyren:123456', 'www.baidu.com')
print(urllib.parse.splitvalue('http://www.baidu.com/index.html?id=1')) # ('http://www.baidu.com/index.html?id', '1')
print(urllib.parse.urlparse('http://www.baidu.com:80/index.html?id=1#tag1'))
# ParseResult(scheme='http', netloc='www.baidu.com:80', path='/index.html', params='', query='id=1', fragment='tag1')
print(urllib.parse.urlsplit('http://www.baidu.com:80/index.html?id=1#tag1'))
# SplitResult(scheme='http', netloc='www.baidu.com:80', path='/index.html', query='id=1', fragment='tag1')
print(urllib.parse.urljoin('http://www.baidu.com/index.php', 'search.php')) # 'http://www.baidu.com/search.php'
print(urllib.parse.urljoin('http://www.baidu.com/hello/index.php', 'search.php')) # 'http://www.baidu.com/hello/search.php'
print(urllib.parse.urljoin('http://www.baidu.com/hello/index.php', '../search.php')) # 'http://www.baidu.com/search.php'
print(urllib.parse.urljoin('http://www.baidu.com/hello/index.php', '/search.php')) # 'http://www.baidu.com/search.php'
print(urllib.parse.urljoin('http://www.baidu.com/hello/index.php', 'http://www.baidu.com/search.php')) # 'http://www.baidu.com/search.php'
print(urllib.parse.urljoin('http://www.baidu.com/hello', 'search.php')) # 'http://www.baidu.com/search.php'
print(urllib.parse.urljoin('http://www.baidu.com/hello/', 'search.php')) # 'http://www.baidu.com/hello/search.php'
print(urllib.parse.urlencode({'name':'rileyren','id':1})) # name=rileyren&id=1
print(urllib.parse.urlencode({'name':'rileyren#','id':1})) # name=rileyren%23&id=1

params = {
	'wd': 'rileyren'
}

print(urllib.request.urlopen('http://www.baidu.com/s?' + urllib.parse.urlencode(params)).read().decode('gbk'))
print(urllib.request.urlopen('http://www.baidu.com/s', urllib.parse.urlencode(params).encode('utf-8')).read().decode('gbk'))
req = urllib.request.Request(url = 'http://www.baidu.com/', data = urllib.parse.urlencode(params).encode('utf-8'), headers = {
	'Host': 'www.baidu.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
})
print(urllib.request.urlopen(req).read().decode('gbk'))


cj = http.cookiejar.CookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=cnhiMTIzZGV2JTQwc2luYS5jb20%3D&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.5)&_=1362121822029'
print(opener.open(url).read().decode('utf-8'))

