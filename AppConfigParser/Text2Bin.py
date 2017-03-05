#coding:utf-8
# #! /bin/python
import os
import sys
import os.path
import pickle
import  struct
import binascii
import xml.etree.ElementTree as ET

dirroot = "F:\\feature_train\\"
newdirroot="F:\\new\\"
for dirnames in os.listdir(dirroot):
    print ("进入文件夹:" )
    #print dirnames
    for dirname in os.listdir(dirroot+dirnames):
        #print dirname
        if dirname.split('.')[1]!='xml':
            continue
        tree = ET.parse("AndroidManifest_2.xml")     #打开xml文档
        #root = ET.fromstring(country_string) #从字符串传递xml
        root = tree.getroot()         #获得root节点
        data = binascii.a2b_qp(ET.tostring(root, pretty_print=True))
        fileNew=open(newdirroot+dirnames+'\\'+"aaa.xml",'wb')
        fileNew.write(data)
        fileNew.write('\n')
        fileNew.close()