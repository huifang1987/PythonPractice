import os
import boto3
from itertools import islice
from boto3.session import Session

LOCAL_DIR = '/mnt/Log/home/logs'

aws_key = "AKIAPR624H5FHL6MNBGA"

aws_secret = "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"

session = Session(aws_access_key_id=aws_key,aws_secret_access_key=aws_secret, region_name='cn-north-1')
s3 = session.resource('s3')

bucket = s3.Bucket('links')
for b in bucket.objects.all():
        if "#" not in b.key or ".zip" not in b.key:
                b.delete()
                continue
        dirs = b.key.split('#')
        print(b.key)
        print(dirs)
        currentDir = LOCAL_DIR
        for dir in dirs :
                print(dir)
                if ".zip" in dir:
                        s3.meta.client.download_file('links',b.key,dir)
                        b.delete()
                else :
                        currentDir = currentDir+"/"+dir
                        if os.path.exists(currentDir) == False :
                                os.mkdir(currentDir)
                        os.chdir(currentDir)


