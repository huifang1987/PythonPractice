#!/usr/bin/env python
import os
import sys
import re
import xml.etree.ElementTree as ET
if len(sys.argv) < 4 :
        sys.exit(0)
path1 = sys.argv[1]
path2 = sys.argv[2]
version = sys.argv[3]
path = path1 + "/" + path2
whitelist = ["CircleWindow","CookieLauncher","VideoCall","DynamicDomain","RemoteContact"
,"DigitalCalendar","Notification","HomeWeather","SetupWazard","News","MusicPlayer","netMedia"
,"Notepad","MMTool","Clock","Miracast","VoiceAssistant","QLoveService"]
if "packages" not in path2:
        sys.exit(0)
if path2.split('/')[2] not in whitelist:
	print(path2.split('/')[2]+" not in whitelist")
	sys.exit(0)
if version.count("-") < 2 :
        sys.exit(0)
subVersion = version.split('-')[2]
if subVersion.count(".") < 3 :
	sys.exit(0)
os.chdir(path)
output = os.popen("git rev-list --all --count")
count = int(output.read())
a = subVersion.split('.')[0]
b = subVersion.split('.')[1]
c = subVersion.split('.')[2]
d = subVersion.split('.')[3]
if a.isdigit() == False or b.isdigit() == False or c.isdigit() == False or d.isdigit() == False :
	sys.exit(0)
if len(a) > 1 or len(b) > 1 or len(c) > 1 or len(d) >2 or len(str(count))>4 :
	sys.exit(0)
versionCode = a+b+c+d.zfill(2)+str(count).zfill(4)
versionName = version
fileName = path+"/AndroidManifest.xml"
ET.register_namespace('android', "http://schemas.android.com/apk/res/android")
if os.path.exists(fileName) :
        tree = ET.parse(fileName)
        root = tree.getroot()
        root.set('{http://schemas.android.com/apk/res/android}versionCode',str(versionCode))
        root.set('{http://schemas.android.com/apk/res/android}versionName',versionName)
        tree.write(fileName)

#f=open(path + "/debug.txt","w+")
#f.write(str(count)+"\n")
#f.write(version+"\n")
#f.write("subVersion = "+subVersion+"\n")
#f.close()

