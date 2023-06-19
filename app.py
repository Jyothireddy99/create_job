from aws_cdk import App, Tags, Environment

from config import *
from tags import TAGS
from envs import REGION
from infra import DeploymentStack 

app = App()

for tag_name, tag_value in TAGS.items():
    Tags.of(app).add(tag_name, tag_value)

env = Environment(
    account=ACCOUNT_ID, 
    region=REGION
)

DeploymentStack(
    app, 
    STACK_NAME,
    description=STACK_DESCRIPTION,
    env=env
)

app.synth()
