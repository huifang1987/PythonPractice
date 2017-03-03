#!/usr/bin/env python
import os
import shutil
import sys
import xml.etree.ElementTree as ET
if len(sys.argv) < 4 :
        sys.exit(0)
path1 = sys.argv[1]
path2 = sys.argv[2]
path = path1 + "/" + path2
SOUR_PATH = path+"/"
DEST_PATH = path+"/temp/"
version = sys.argv[3]
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
whiteList = ["Links.apk","QLove.apk","QLoveSocket.apk","AnalyticsServiceSDKLib.apk","BlueTester.apk"]
if a.isdigit() == False or b.isdigit() == False or c.isdigit() == False or d.isdigit() == False :
        sys.exit(0)
if len(a) > 1 or len(b) > 1 or len(c) > 1 or len(d) >2 or len(str(count))>4 :
        sys.exit(0)
versionCode = a+b+c+d.zfill(2)+str(count).zfill(4)
versionName = version

children = os.listdir(SOUR_PATH)
for child in children:
        if os.path.isfile(SOUR_PATH+child) and (child in whiteList) :
                if os.path.exists(DEST_PATH) == False:
                        os.mkdir(DEST_PATH)
                intermidate = os.path.join(DEST_PATH,child.split('.')[0])
                os.system("java -jar "+path1+"/build/tools/apktool.jar d "+SOUR_PATH+child+" -fo "+intermidate)
                if os.path.exists(os.path.join(intermidate,"AndroidManifest.xml")) == False:
                        continue
                ET.register_namespace('android', "http://schemas.android.com/apk/res/android")
                tree = ET.parse(os.path.join(intermidate,"AndroidManifest.xml"))
                root = tree.getroot()
                root.set('{http://schemas.android.com/apk/res/android}versionCode',str(versionCode))
                root.set('{http://schemas.android.com/apk/res/android}versionName',versionName)
                tree.write(os.path.join(intermidate,"AndroidManifest.xml"))
                os.system("java -jar "+path1+"/build/tools/apktool.jar b "+intermidate+" -o "+DEST_PATH+child)
                os.system("java -jar "+path1+"/build/tools/signapk.jar "\
                +path1+"/build/target/product/security/platform.x509.pem "\
                +path1+"/build/target/product/security/platform.pk8 "\
                +DEST_PATH+child+" "+SOUR_PATH+child)
                shutil.rmtree(DEST_PATH)

#f=open(path + "/debug.txt","w+")
#f.write(str(count)+"\n")
#f.write(version+"\n")
#f.write("versionCode = "+versionCode+"\n")
#f.write("SOUR_PATH = "+SOUR_PATH+"\n" )
#f.close()
