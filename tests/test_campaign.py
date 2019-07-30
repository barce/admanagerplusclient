import config
import json

import unittest

from admanagerplusclient.connection import Connection
from admanagerplusclient.campaign import Campaign

class CampaignTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = Connection(config.client_id, config.client_secret, config.refresh_token)

    def test_get_all_campaigns_by_advertiser(self):
        c = Campaign(CampaignTestCase.connection)

        campaigns = json.loads(c.get_all_by_advertiser(25063, 92))
        print(campaigns)

        self.assertEqual(campaigns["response_code"], 200)

    def test_get_one_campaign(self):
        c = Campaign(CampaignTestCase.connection)

        campaign = json.loads(c.get_one(97893, 92))
        print(campaign)

        self.assertEqual(campaign["response_code"], 200)
