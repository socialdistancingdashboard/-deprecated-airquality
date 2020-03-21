import requests
import boto3
import os
import json

airquality_token = os.environ['AIR_QUALITY_API_TOKEN']
url = 'https://api.waqi.info/feed/berlin/?token=' + airquality_token

client = boto3.client('kinesis')

response = requests.get(url)
if response.status_code == 200:
    response = client.put_record(StreamName='sdd-kinesis-airquality', Data=json.dumps(response.json(), indent=2, sort_keys=True), PartitionKey='part_key_1')