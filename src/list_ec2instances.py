import json

import boto3
import botocore

from config import CONFIG
from credentials import credential_helper


def handler(event=None, context=None):
    ec2 = create_new_session(event).resource('ec2')
    return any(ec2.instances.iterator())


def create_new_session(event):
    return credential_helper.create_new_session()


if __name__ == "__main__":
    result = handler()
    print(result)
