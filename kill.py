import os
import sys
import re

if len(sys.argv)==1:
	os.exit()

os.system("ps aux | grep "+sys.argv[1]+" >kill.log")
fp=open("kill.log","r")
res=[]
p=re.compile(r"\s+")
for v in fp:
	if v.find("python kill.py")==-1:
		res.append(p.split(v)[1])
fp.close()

print res

for v in res:
	try:
		os.kill(int(v),9)
	except Exception,e:
		print e
	#os.system("kill -9 "+str(v))
print str(len(res)-2)+" progess killed\n"
#shell grep process has been killed,but the pid was stored



