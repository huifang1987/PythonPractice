#!/usr/bin/python
#coding:utf-8

from xml.dom.minidom import Document
import json
import os
try:
  import xml.etree.cElementTree as ET
except ImportError:
  import xml.etree.ElementTree as ET
import sys


tree = ET.parse("AndroidManifest_2.xml")     #打开xml文档
#root = ET.fromstring(country_string) #从字符串传递xml
root = tree.getroot()         #获得root节点
filename = "out.xml"
f = open(filename, "a")


package = root.attrib["package"]
appVersion = root.attrib["{http://schemas.android.com/apk/res/android}versionCode"]
print("package: ",package)
print("appVersion: ",appVersion)
if os.path.exists(filename) :
  f.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
f.write("<app package = "+package+">\n")
f.write("\t<appVersion>"+appVersion+"</appVersion>\n")
for application in root.findall('application'): #找到root节点下的所有country节点
  meta_data = application.find('meta-data')   #子节点下节点rank的值
  name =  meta_data.attrib["{http://schemas.android.com/apk/res/android}name"]
  value = meta_data.attrib["{http://schemas.android.com/apk/res/android}value"]
  config = { name : value }
  print("config: ",config)
  f.write("\t<config>{ "+name+" : "+value+" }</config>\n")
  f.write("</app>\n")
  f.close()
