from unittest import TestCase
from admanagerplusclient import ampclient
import os
import json
import time
from datetime import datetime

class TestBrightRollClient(TestCase):
    def test_config(self):
        b = ampclient.BrightRollClient()
        self.assertTrue(isinstance(b, ampclient.BrightRollClient))

    def test_traffic_types(self):
        b = ampclient.BrightRollClient()
        b.token = os.environ['BR_TOKEN']
        traffic_types = b.traffic_types('campaigns?accountId=20500')
        self.assertTrue('"msg_type": "success"', traffic_types)

    def test_traffic_type_by_id(self):
        b = ampclient.BrightRollClient()
        b.token = os.environ['BR_TOKEN']
        traffic_type_by_id = b.traffic_type_by_id('campaigns', 20500)
        self.assertTrue('"msg_type": "success"', traffic_type_by_id)

    def test_traffic_types_by_filter(self):
        b = ampclient.BrightRollClient()
        b.token = os.environ['BR_TOKEN']
        traffic_types_by_filter = b.traffic_types_by_filter('campaigns', 20500)
        self.assertTrue('"msg_type": "success"', traffic_types_by_filter)

    def test_update_traffic_type(self):
        b = ampclient.BrightRollClient()
        b.token = os.environ['BR_TOKEN']
        # get campaign
        campaign = b.traffic_type_by_id('campaigns', 86184)
        # convert json obj back to python obj
        campaign = json.loads(campaign)['data']['response']
        # update name of campaign for testing purposes
        hash_campaign = {
            "response": {
                "status": campaign['status'],
                "goalType": campaign['goalType'],
                "name": "Matt BR 2018 Test 1sss",
                "goalValue": campaign['goalValue'],
                "budget": campaign['budget'],
                "accountId": campaign['accountId'],
                "totalBudgetType": campaign['totalBudgetType'],
                "dailyBudget": campaign['dailyBudget']
            }
        }
        updated_traffic_type = b.update_traffic_type("campaigns", 86184, hash_campaign)
        self.assertTrue('"msg_type": "success"', updated_traffic_type)

    def test_create_traffic_type(self):
        b = ampclient.BrightRollClient()
        b.token = os.environ['BR_TOKEN']
        start_date = str(datetime.now()).split(' ')[0]
        hash_campaign = {
            "name": "arun test campaign",
            "campaignStartDate": "2018-02-20",
            "status": "ACTIVE",
            "goalType": "CTR",
            "goalValue": 1.0,
            "totalBudgetType": "UNLIMITED",
            "accountId": 29601
        }

        new_traffic_type = b.create_traffic_type("campaigns", hash_campaign)
        self.assertTrue('"msg_type": "success"', new_traffic_type)