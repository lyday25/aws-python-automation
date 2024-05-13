import json
import boto3

def lambda_handler(event, context):
    
    print('connecting to Iam ')
    iam=boto3.resource('iam')
    group=iam.Group('managers').users.all()
    #create list of users
    print('list of users')
    names=[i.name for i in group]
    return names

