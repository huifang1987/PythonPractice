# -*- coding: gb18030 -*-
import Spider
import sys
import time
import random

s=Spider.Spider()
#����
year=int(sys.argv[1])
for month in [1,2,3,4,5,6,7,8,9,10,11,12]:
    delta=s.timeDelta(year,month)
    #һ����һ���µ�ץȡ
    day =1
    while day<=delta:
        #����
        date=s.handleDate(year,month,day)
        #ҳ��
        allNum=s.getAllNum(date)
        while allNum == 200:
            print ("I suspect there is not as many as 200 pages in one day. Let's try again!")
            time.sleep(random.random())
            allNum = s.getAllNum(date)
        allLinks = s.getAllLinks(allNum, date)
        while len(allLinks) <= 30 * (allNum - 1) or len(allLinks) > 30 * allNum:
            print ("I suspect at least "+str(30*(allNum-1)-len(allLinks)+1)+" is lost! Try again!")
            time.sleep(random.random())
            allNum = s.getAllNum(date)
            allLinks = s.getAllLinks(allNum, date)
        #��Ϣ
        s.saveAllInfo(allLinks,date)
        day+=1
        print date,'Finished!'
print date.strftime('%Y-%m'),'KO!'