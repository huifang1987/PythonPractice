import oss2
import os
from itertools import islice

LOCAL_DIR = '/mnt/Log/home/logs'

auth = oss2.Auth('T46xHl8KZy5zNu3A', 'eZAMizDtEAoQI1HlpQ3IIMbcXuqXId')
service = oss2.Service(auth, 'http://oss-cn-qingdao.aliyuncs.com')
bucket = oss2.Bucket(auth, 'http://oss-cn-qingdao.aliyuncs.com', 'szjy-qlove-links')
print(bucket)
for b in islice(oss2.ObjectIterator(bucket),1000):
    dirs = b.key.split('&')
    print(b.key)
    print(dirs)
    currentDir = LOCAL_DIR
    for dir in dirs :
        print(dir)
        if ".zip" in dir :
            bucket.get_object_to_file(b.key,dir)
            bucket.delete_object(b.key)
        else :
            currentDir = currentDir+"/"+dir
            if os.path.exists(currentDir) == False :
                os.mkdir(currentDir)
            os.chdir(currentDir)
