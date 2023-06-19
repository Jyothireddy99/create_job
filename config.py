import boto3
sts = boto3.client('sts')

from envs import PROJECT


STACK_NAME = "".join(PROJECT.split())
STACK_DESCRIPTION = " ".join([PROJECT, "Stack"])

ACCOUNT_ID = sts.get_caller_identity()['Account']
