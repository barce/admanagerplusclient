import config
import json

import unittest

from admanagerplusclient.connection import Connection
from admanagerplusclient.advertiser import Advertiser

class AdvertiserTestCase(unittest.TestCase):
    def test_get_advertisers(self):
        c = Connection(config.client_id, config.client_secret, config.refresh_token)
        a = Advertiser(c)

        advertisers = json.loads(a.traffic_types('advertisers', 92))

        print(advertisers)

        self.assertEqual(advertisers["response_code"], 200)
