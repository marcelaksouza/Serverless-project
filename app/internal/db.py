import os
import boto3
import pathlib
from dotenv import load_dotenv
from boto3.resources.base import ServiceResource

base_dir = pathlib.Path(__file__).parent.parent.parent

load_dotenv(base_dir.joinpath('.env'))

class Config:
    DB_ENDPOINT = os.getenv('DB_ENDPOINT')
    DB_REGION_NAME = os.getenv('DB_REGION_NAME')
    DB_ACCESS_KEY_ID = os.getenv('DB_ACCESS_KEY_ID')
    DB_SECRET_ACCESS_KEY = os.getenv('DB_SECRET_ACCESS_KEY')

def Initialize_db() -> ServiceResource:
    ddb = boto3.resource('dynamodb',
                        endpoint_url=Config.DB_ENDPOINT,
                        region_name=Config.DB_REGION_NAME,
                        aws_access_key_id=Config.DB_ACCESS_KEY_ID,
                        aws_secret_access_key=Config.DB_SECRET_ACCESS_KEY
                        )
    print("DB connected")
    return ddb