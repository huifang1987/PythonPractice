# -*- coding: gb18030 -*-
import Spider
import sys
import time
import random

s=Spider.Spider()
#日期
#year=int(sys.argv[1])
#month=int(sys.argv[2])
#day=int(sys.argv[3])
year = 2004
month = 5
day = 1
delta=s.timeDelta(year,month)
#一个月一个月的抓取
while day<=delta:
    #日期
    date=s.handleDate(year,month,day)
    #页数
    allNum=s.getAllNum(date)
    while allNum == 200:
        print ("I suspect there is not as many as 200 pages in one day. Let's try again!")
        time.sleep(random.random())
        allNum = s.getAllNum(date)
    allLinks = s.getAllLinks(allNum, date)
    while len(allLinks) <= 30 * (allNum - 1) or len(allLinks) > 30 * allNum:
        print ("I suspect at least "+str(30*(allNum-1)-len(allLinks))+"is lost! Try again!")
        time.sleep(random.random())
        allNum = s.getAllNum(date)
        allLinks = s.getAllLinks(allNum, date)
    #信息
    s.saveAllInfo(allLinks,date)
    day+=1
    print date,'Finished!'
print date.strftime('%Y-%m'),'KO!'
