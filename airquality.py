import requests
import boto3
import os
import json




url = 'https://api.waqi.info/feed/berlin/?token='+os.environ['AIR_QUALITY_API_TOKEN']

response = requests.get(url)
response_json=response.json()

print(json.dumps(response_json, indent=2, sort_keys=True))

if response.status_code == 200:
    client = boto3.client('kinesis')
    #Records = [{"Data" : json.dumps(response_json, indent=2, sort_keys=True)}
    response = client.put_record(StreamName='sdd-kinesis-airquality', Data=json.dumps(response_json, indent=2, sort_keys=True),PartitionKey='part_key_1')
    print (response)