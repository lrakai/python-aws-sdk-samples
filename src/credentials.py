import boto3

from config import CONFIG


class credential_helper:
    def create_new_session(self):
        return boto3.Session(
        aws_access_key_id = CONFIG['client_id'],
        aws_secret_access_key = CONFIG['client_secret'],
      	region_name = CONFIG['region_name']
    )