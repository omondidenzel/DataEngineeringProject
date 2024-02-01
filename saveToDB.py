import boto3
from dataEtl import AWS_ACCESS_KEY_ID,AWS_DEFAULT_REGION,AWS_SECRET_ACCESS_KEY

def saveToDBFunc():
    #read data from s3 bucket
    try:
        s3 = boto3.resource(
                service_name='s3',
                region_name=AWS_DEFAULT_REGION,
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY
            )
        print(s3.bucket.all())
    except:
        print('Not connected to S3')
#saveToDBFunc()