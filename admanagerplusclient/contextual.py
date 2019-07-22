#!/usr/bin/env python

import json
import requests
import base64

import sys

# if sys.version_info < (3, 0):
#     raise "must use python 2.5 or greater"

use_environment_variables = None

try:
    from django.conf import settings
except ImportError:
    use_environment_variables = True
    

class Contextual:
    id = None
    name = None
    accountId = 0
    br_client = None
    taxonomyType = None
    categories = {
        "categories": [
            {
                "categoryId": 0
            },
        ]
    }
    updatedAt = None

    def __init__(self, br_client):
        self.br_client = br_client

    def read_by_id(self, cid):
        headers = {'Content-Type': 'application/json', 'X-Auth-Method': 'OAUTH',
                   'X-Auth-Token': str(self.br_client.raw_token_results['access_token'])}
        url = self.br_client.dsp_host + "/traffic/contextuals"
        url = url + "/" + str(cid)

        result = requests.get(url, headers=headers)
        traffic_type = result.json()
        try:
            if traffic_type['errors']['httpStatusCode'] == 401:
                refresh_results_json = self.br_client.refresh_access_token()
        except:
            print("expected result")
        return traffic_type

    def update(self, cid, lists):
        headers = {'Content-Type': 'application/json', 'X-Auth-Method': 'OAUTH',
                   'X-Auth-Token': str(self.raw_token_results['access_token'])}
        r = requests.put(self.dsp_host + "/traffic/contextuals/" + str(cid), data=lists, headers=headers)
        results = r.json()
        try:
            if results['errors']['httpStatusCode'] == 401:
                refresh_results_json = self.refresh_access_token()
        except:
            print("expected result")

        return r

    def create(self, s_type, lists):
        headers = {'Content-Type': 'application/json', 'X-Auth-Method': 'OAUTH',
                   'X-Auth-Token': str(self.raw_token_results['access_token'])}
        r = requests.post(self.dsp_host + "/traffic/contextuals", data=lists, headers=headers)
        results = r.json()
        try:
            if results['errors']['httpStatusCode'] == 401:
                refresh_results_json = self.refresh_access_token()
        except:
            print("expected result")
        return r
