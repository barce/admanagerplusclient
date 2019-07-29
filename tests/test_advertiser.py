import config
import json

import unittest

from admanagerplusclient.connection import Connection
from admanagerplusclient.advertiser import Advertiser

class AdvertiserTestCase(unittest.TestCase):
    def test_get_all_advertisers(self):
        c = Connection(config.client_id, config.client_secret, config.refresh_token)
        a = Advertiser(c)

        advertisers = json.loads(a.traffic_types('advertisers', 92))

        self.assertEqual(advertisers["response_code"], 200)

    def test_get_one_advertiser(self):
        c = Connection(config.client_id, config.client_secret, config.refresh_token)
        a = Advertiser(c)

        advertiser = json.loads(a.traffic_type_by_id('advertisers', 25063, 92))

        print(advertiser)

        self.assertEqual(advertiser["response_code"], 200)
        self.assertEqual(advertiser["data"]["response"]["name"], "Hawaii Tourism")
