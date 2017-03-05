#!/usr/bin/python
#coding:utf-8

import os
import shutil
import sys
from xml.dom.minidom import Document
import json
import xml.etree.ElementTree as ET

SOUR_PATH = "/home/fanghui/Discovery/LINUX/android/out/target/product/msm8916_64/system/priv-app/"
DEST_PATH = "/home/fanghui/ConfigParser/temp/"
SOUR_PATH2 = "/home/fanghui/Discovery/LINUX/android/out/target/product/msm8916_64/system/app/"




parents = os.listdir(SOUR_PATH)
for parent in parents:
  if os.path.isdir(SOUR_PATH+parent) == True:
    children = os.listdir(SOUR_PATH+parent)
    print(parent)
    for child in children:
      if os.path.isfile(SOUR_PATH+parent+"/"+child) and (".apk" in child):
        if os.path.exists(DEST_PATH) == False:
          os.mkdir(DEST_PATH)
        shutil.copy(SOUR_PATH+parent+"/"+child,DEST_PATH+child)
        os.system("unzip "+DEST_PATH+child+" -d "+DEST_PATH+"Decompressed")
        os.system("java -jar AXMLPrinter2.jar "+DEST_PATH+"Decompressed/AndroidManifest.xml > "+DEST_PATH+"Decompressed/AndroidManifest_2.xml")
        tree = ET.parse(DEST_PATH+"Decompressed/AndroidManifest_2.xml")
        root = tree.getroot()
        filename = "out.xml"
        f = open(filename, "a")
        if os.path.getsize(filename)== 0 :
          f.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
        package = root.attrib["package"]
        appVersion = root.attrib["{http://schemas.android.com/apk/res/android}versionCode"]
        print("package: ",package)
        print("appVersion: ",appVersion)
        if os.path.exists(filename) :
          for application in root.findall('application'):
#           meta_data = application.find('meta-data')
            flag = 0
            for meta_data in application.findall('meta-data'):
              name =  meta_data.attrib["{http://schemas.android.com/apk/res/android}name"]
              value = meta_data.attrib["{http://schemas.android.com/apk/res/android}value"]
              if "UMS_" in name :
                if flag == 0:
                  f.write("<app package = "+package+">\n")
                  f.write("\t<appVersion>"+appVersion+"</appVersion>\n")
                config = { name : value }
                print("config: ",config)
                f.write("\t<config>{ "+name+" : "+value+" }</config>\n")
                flag = flag + 1
          if flag > 0 :
            f.write("</app>\n")
          f.close()
    shutil.rmtree(DEST_PATH,True)

parents = os.listdir(SOUR_PATH2)
for parent in parents:
  if os.path.isdir(SOUR_PATH2+parent) == True:
    children = os.listdir(SOUR_PATH2+parent)
    print(parent)
    for child in children:
      if os.path.isfile(SOUR_PATH2+parent+"/"+child) and (".apk" in child):
        if os.path.exists(DEST_PATH) == False:
          os.mkdir(DEST_PATH)
        shutil.copy(SOUR_PATH2+parent+"/"+child,DEST_PATH+child)
        os.system("unzip "+DEST_PATH+child+" -d "+DEST_PATH+"Decompressed")
        os.system("java -jar AXMLPrinter2.jar "+DEST_PATH+"Decompressed/AndroidManifest.xml > "+DEST_PATH+"Decompressed/AndroidManifest_2.xml")
        tree = ET.parse(DEST_PATH+"Decompressed/AndroidManifest_2.xml")
        root = tree.getroot()
        filename = "out.xml"
        f = open(filename, "a")
        if os.path.getsize(filename)== 0 :
          f.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
        package = root.attrib["package"]
        appVersion = root.attrib["{http://schemas.android.com/apk/res/android}versionCode"]
        print("package: ",package)
        print("appVersion: ",appVersion)
        if os.path.exists(filename) :
          for application in root.findall('application'):
#           meta_data = application.find('meta-data')
            flag = 0
            for meta_data in application.findall('meta-data'):
              name =  meta_data.attrib["{http://schemas.android.com/apk/res/android}name"]
              value = meta_data.attrib["{http://schemas.android.com/apk/res/android}value"]
              if "UMS_" in name :
                if flag == 0:
                  f.write("<app package = "+package+">\n")
                  f.write("\t<appVersion>"+appVersion+"</appVersion>\n")
                config = { name : value }
                print("config: ",config)
                f.write("\t<config>{ "+name+" : "+value+" }</config>\n")
                flag = flag + 1
          if flag > 0 :
            f.write("</app>\n")
          f.close()
    shutil.rmtree(DEST_PATH,True)
