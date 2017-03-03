#!/usr/bin/python
# coding=utf-8

import ftplib
import os
import socket
import time
import logging
import zipfile

HOST = '203.100.94.151'
PORT = 22211
USERNAME = 'thundersoft'
PASSWORD = 'haothunder'
ROOT_DIR = '/Thundersoft/Discovery/ImageRelease/DailyBuild/'
LOCAL_DIR = './'
LOG_FILE = './GetImage.log'
UNZIP_DIR = LOCAL_DIR + 'LastImgDebug/'
CURR_DATE = time.strftime('%Y%m%d',time.localtime(time.time()))
CURR_DATE = str(20111111)

def main():
    global CURR_DATE
    logging.basicConfig(filename = LOG_FILE, level = logging.DEBUG)
    current_date =  CURR_DATE

    try:
        ftp = ftplib.FTP()
	ftp.connect(HOST,PORT)
    except ftplib.error_perm:
        print('无法连接到"%s"' % HOST)
        logging.error('无法连接到"%s"' % HOST)
        return
    print('-----------------------------------------------\n连接到"%s"' % HOST)
    logging.debug('连接到"%s"' % HOST)

    try:
        ftp.login(USERNAME,PASSWORD)
    except ftplib.error_perm:
        print('登录失败')
        logging.debug('登录失败')
        ftp.quit()
        return
    print('登陆成功')
    logging.debug('登陆成功')

    try:
       #得到DIRN的工作目录
        ftp.cwd(ROOT_DIR + current_date)
    except ftplib.error_perm:
        print('列出当前目录失败')
        logging.error('列出当前目录失败')
        ftp.quit()
        return
    print(ftp.nlst())
    dirlist = ftp.nlst()
    try:
        os.getcwd()
  	if os.path.exists(LOCAL_DIR + current_date) == False:
            os.mkdir(LOCAL_DIR + current_date)
        os.chdir(LOCAL_DIR + current_date)
	logging.debug ('Start download: '+time.strftime('%Y%m%d_%H:%M:%S',time.localtime(time.time())))
        for DIR in dirlist:
              	if os.path.exists(DIR) == False:
                    os.mkdir(DIR)
                    os.chdir(DIR)
                    ftp.cwd(DIR)
                    downloadlist = ftp.nlst()
                    for FILE in downloadlist:
                        ftp.retrbinary('RETR %s' % FILE,open(FILE,'wb').write)
                        print('文件"%s"下载成功' % FILE)
                        logging.debug('文件"%s"下载成功' % FILE)
                        print(os.getcwd())
                    os.chdir(LOCAL_DIR + current_date)
    except ftplib.error_perm:
        print('无法读取"%s"' % FILE)
        logging.error('无法读取"%s"' % FILE)
        os.unlink(FILE)
    else:
        print('文件全部下载完毕！')
        logging.debug('文件全部下载完毕！\n------------------------------------------------')
	logging.debug ('Finish download: '+time.strftime('%Y%m%d_%H:%M:%S',time.localtime(time.time())))
        ftp.quit()
        return

def unzipimg():
    global CURR_DATE
    global UNZIP_DIR
    path = LOCAL_DIR + CURR_DATE + '/ZX_Build/'
    if os.path.exists(path) == False:
        return
    files = os.listdir(path)
    for item in files:
        zipname = path + item
        r = zipfile.is_zipfile(zipname)
        print r
        if "-D-" in item and r:
            print zipname
            zf = zipfile.ZipFile(zipname,'r')
            for filename in zf.namelist():
                zf.extract(filename,UNZIP_DIR)
    print 'extract log to:' + UNZIP_DIR + ' !'
    logging.debug('Extract log to:' + UNZIP_DIR + ' !')

if __name__ == '__main__':
    main()
    unzipimg()
