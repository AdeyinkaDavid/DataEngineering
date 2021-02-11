##Code to run a lambda function that will create a CF Stack from a CF Template in an s3 bucket 

import boto3
cf_client = boto3.client('cloudformation')
cf_client.create_stack(
    StackName='my-stack',
    TemplateURL='https://isaacdataprocess.s3.amazonaws.com/emrpractice/createemr.json'
)