import boto3
import json
import pprint

session=boto3.session.Session(profile_name="default")
#ec2_console_resource=boto3.resource(service_name="ec2",region_name="us-east-1")
ctrail_client = boto3.client("cloudtrail")
response = ctrail_client.lookup_events(LookupAttributes=[
        {
            #'AttributeKey': 'EventId'|'EventName'|'ReadOnly'|'Username'|'ResourceType'|'ResourceName'|'EventSource'|'AccessKeyId',
            'AttributeKey':'EventName',
            'AttributeValue': 'CreateBucket'
        }
    ]
   
    
    )

response1 = ctrail_client.lookup_events(LookupAttributes=[
        {
            #'AttributeKey': 'EventId'|'EventName'|'ReadOnly'|'Username'|'ResourceType'|'ResourceName'|'EventSource'|'AccessKeyId',
            'AttributeKey':'EventName',
            'AttributeValue': 'CreateUser'
        }
    ]
   
    
    )
#response['Events'].append(response1)
#print(response)
#event['Events'][0]['Username']
print(response['Events'][1]['Username'])
#print(response)