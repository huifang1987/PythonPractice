#!/usr/bin/env python3
import os
import sys
import time
try:
	import requests
except ImportError:
	os._exit(0)


BUILD_VERSION = sys.argv[1]
IMAGE_TYPE = sys.argv[2]
CURR_DATE = time.strftime('%Y-%m-%d',time.localtime(time.time()))
VERSION_NAME = BUILD_VERSION+"_"+IMAGE_TYPE+"_unsigned"
USERNAME="generate_version"
PASSWD = "szjynanjing"

if "Q8611-2137.1-" in BUILD_VERSION and "debug" in IMAGE_TYPE:
	filePath = "/01.FtpFolder/01.CIBuild/Q8611/qlove-8939-lp50-dev/"+BUILD_VERSION+"/"+IMAGE_TYPE+"/"+VERSION_NAME+".zip"
	url = 'http://58.213.63.61:9002/index.php?m=build&f=create&project=22'
	branch = 15
elif "Q8311-2137.1-" in BUILD_VERSION and "debug" in IMAGE_TYPE:
        filePath = "/01.FtpFolder/01.CIBuild/Q8311/qlove-8939-lp50-dev/"+BUILD_VERSION+"/"+IMAGE_TYPE+"/"+VERSION_NAME+".zip"
        url = 'http://58.213.63.61:9002/index.php?m=build&f=create&project=22'
	branch = 15
else:
	os._exit(0)

values = {'product':'1'
	 ,'branch':branch
         ,'name':VERSION_NAME
         ,'builder':USERNAME
         ,'date':CURR_DATE
         ,'filePath':filePath}
print (str(values))
resp = requests.post(url, values, auth=(USERNAME, PASSWD))
print (str(resp))
