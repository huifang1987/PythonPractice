# -*- coding: gb18030 -*-
import Spider
import sys
import time
import random
import threading

s = Spider.Spider()
# ����
# year=int(sys.argv[1])
# month=int(sys.argv[2])
# day=int(sys.argv[3])
year = 2012
month = 12
day = 3
delta = s.timeDelta(year, month)


# һ����һ���µ�ץȡ
def get(year, month, day):
    # ����
    date = s.handleDate(year, month, day)
    # ҳ��
    try:
        allNum = s.getAllNum(date)
    except Exception as e:
        print e
    while allNum == 200:
        print ("I suspect there is not as many as 200 pages in one day. Let's try again!")
        time.sleep(random.random())
        allNum = s.getAllNum(date)
    allLinks = s.getAllLinks(allNum, date)
    while len(allLinks) <= 30 * (allNum - 1) or len(allLinks) > 30 * allNum:
        print ("I suspect at least " + str(30 * (allNum - 1) - len(allLinks)) + "is lost! Try again!")
        time.sleep(random.random())
        allNum = s.getAllNum(date)
        allLinks = s.getAllLinks(allNum, date)
    # ��Ϣ
    s.saveAllInfo(allLinks, date)
    print date, 'Finished!'


threads = []
while day <= delta:
    workThread = threading.Thread(target=get,args=(year, month, day))
    threads.append(workThread)
    day+=1

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
