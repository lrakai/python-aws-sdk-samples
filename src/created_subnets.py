import json

import boto3
import botocore

from config import CONFIG
from credentials import credential_helper


def handler(event=None, context=None):
    lab_step_variable = int(2)
    
    ec2 = create_new_session(event).resource('ec2')
    return any(not vpc.is_default and len(list(vpc.subnets.iterator())) >= lab_step_variable for vpc in ec2.vpcs.iterator())


def create_new_session(event):
    return credential_helper.create_new_session()


if __name__ == "__main__":
    result = handler()
    print(result)
