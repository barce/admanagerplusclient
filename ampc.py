#!/usr/bin/env python
import json
import jwt
import requests
import time
import os

# os.environ['AOP_CLIENT_ID']
# os.environ['AOP_CLIENT_SECRET']
# os.environ['AOP_API_KEY']

client_id = os.environ['AOP_CLIENT_ID']
client_secret = os.environ['AOP_CLIENT_SECRET']

host = "id.corp.aol.com"

now = int(time.time())


payload = {
    "aud": "https://{0}/identity/oauth2/access_token?realm=aolcorporate/aolexternals".format(host),
    "iss": client_id,
    "sub": client_id,
    "exp": now + 3600,
    "iat": now ,
}

encoded = jwt.encode(payload, client_secret, algorithm='HS256')

print "ENC",encoded


url = "https://{0}/identity/oauth2/access_token".format(host)

payload = "grant_type=client_credentials&scope=one&realm=aolcorporate/aolexternals&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer&client_assertion={0}".format(encoded)

print "URL",url

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

response = requests.post(url, headers=headers, data=payload)


print "RESPONSE",response.text


json_response = json.loads(response.text)

print "TOKEN",json_response

headers = {'Authorization': "Bearer " + json_response['access_token']}
#headers = {'Authorization': json_response['access_token']}                                                                                                                                               
headers['Content-Type'] = 'application/json'
headers['x-api-key'] = os.environ['AOP_API_KEY']

print "HEADERS",headers

url = "https://api.one.aol.com/advertiser/organization-management/v1/organizations/"

response = requests.get(url, headers=headers, verify=False)
print "RESPONSE",response.text

url = "https://api.one.aol.com/advertiser/campaign-management/v1/organizations/{0}/advertisers/campaigns".format("7000095690")

response = requests.get(url, headers=headers, verify=False)


print "RESPONSE 2",response.text


url = "https://api.one.aol.com/advertiser/campaign-management/v1/organizations/{0}/advertisers/{1}/campaigns".format("7000095690", "7000095690")

response = requests.get(url, headers=headers, verify=False)

print "RESPONSE 2.5",response.text



url = "https://api.one.aol.com/advertiser/campaign-management/v1/organizations/{0}/advertisers/{1}/campaigns/{2}".format("7000095690", "7000095690", "131210756")

response = requests.get(url, headers=headers, verify=False)

print "RESPONSE 3",response.text



"""                                                                                                                                                                                                       
URL: https://api.one.aol.com/advertiser                                                                                                                                                                   
API key: os.environ['AOP_API_KEY']

"""
