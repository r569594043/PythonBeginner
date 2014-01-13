from bs4 import BeautifulSoup as bs
'''
	HomePage: http://www.crummy.com/software/BeautifulSoup/
	Download: http://www.crummy.com/software/BeautifulSoup/bs4/download/
	Documentation: http://www.crummy.com/software/BeautifulSoup/bs4/doc/
	Doc Chinese: http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
'''

html_doc = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
	<title>Sample</title>
</head>
<body>
	<a href="http://www.google.com/">google<b>bold</b></a>
	<a href="http://www.baidu.com/" class="baidu">baidu</a>
	<a href="http://cn.bing.com/">bing</a>
	<a href="http://weibo.com/">weibo</a>
	<a href="http://t.qq.com/">tqq</a>
	<div class="container main">
		<a href="http://www.google.com/index.php" name="google">google index<b>bold</b></a>
		<a href="http://www.baidu.com/index.php">baidu index</a>
		<a href="http://cn.bing.com/index.php">bing index</a>
		<a href="http://weibo.com/index.php">weibo index</a>
		<a href="http://t.qq.com/index.php">tqq index</a>
	</div>
</body>
</html>"""

bs_doc = bs(html_doc)
for a in bs_doc.find_all('a'):
	print(a.get('href'))
	print(a['href'])
	print(a.text)
	print(a.get_text())
	print(a.string)
a = bs_doc.find('a')
print(a) # <a href="http://www.google.com/">google</a>
