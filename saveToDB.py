import boto3, s3fs
import os
from dotenv import load_dotenv #, dotenv_values

load_dotenv()
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION')

def saveToDBFunc():
    #read data from s3 bucket
    try:
        s3 = boto3.resource(
                service_name='s3',
                region_name=AWS_DEFAULT_REGION,
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY
            )
        for x in s3.buckets.all():
            print(x)
    except:
        print('Not connected to S3')
saveToDBFunc()