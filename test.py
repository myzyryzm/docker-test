import boto3
import os
import sys

s3 = boto3.client('s3')

video = sys.argv[1]
try:
    with open(video, 'rb') as f:
        s3.put_object(Body=f, Bucket='evt-lect-dev-test', Key='video.mp4')
except:
    print('error')

