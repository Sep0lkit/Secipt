# LFI.TESTER
	--simple LFI Tester
---

####Usage:
	LFI.TESTER.py -t [-d] [-f] [-k] [-b] [-n]
	The vuln url will auto-saved into out.txt
####Description:
		-t,--target The test url

		-d,--depth 	The depth for test (Default is 6)	

		-f,--file The File include  (Default is robots.txt)

		-k,--keyword	the keyword for vuln check (Default is User-agent)

		-b,--break-test use advanced block payload test, level(1-8) default is 1

		-n,--no-break	no break while the vuln  finded
