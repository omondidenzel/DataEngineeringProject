import pandas as pd
from datetime import datetime
from dotenv import load_dotenv #, dotenv_values
import logging
import requests
import sys, os
import boto3, s3fs

load_dotenv()
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION')

response = requests.get("https://eodhd.com/api/eod/MCD.US?api_token=demo&fmt=json")
print(response)

logging.basicConfig(stream=sys.stdout, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)

def runEtl():
    try:
        if response.status_code == 200:
            #print(response.status_code)
            #print("Status connected")
            df_list = []
            for data in response.json():
                #print(data)
                df_refined = {
                    "date": data['date'], 
                    "open": data['open'],
                    "high": data['high'],
                    "low": data['low'],
                    "close": data['close'],
                    "adjusted_close": data['adjusted_close'],
                    "volume": data['volume']
                }

                df_list.append(df_refined)
    except:
        log.info("Connection issue")
    finally:
        if len(df_list) > 0:
            #print("Got file")
            df = pd.DataFrame(df_list)
            #Save to local directory
            df.to_csv("extracted.csv",index=False)
            #Save to S3 bucket
            s3 = boto3.resource(
                service_name='s3',
                region_name=AWS_DEFAULT_REGION,
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY
            )

            s3.Bucket('airflow-bucket-denzel').upload_file(
                    Filename="extracted.csv",
                    Key='extracted.csv'
            )

            log.info("CSV file created with data")
        else:
            log.info("No data check code")
runEtl()


