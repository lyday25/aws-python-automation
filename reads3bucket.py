import json
import boto3

def lambda_handler(event, context):
    
    print('connecting to s3 bucket')
    s3=boto3.resource('s3')
    mybucket=s3.Bucket('lydaybucket')
    for i in mybucket.objects.all():
        print(i)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
