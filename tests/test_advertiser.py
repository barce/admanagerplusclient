import config
import json

import unittest

from admanagerplusclient.base import Base
from admanagerplusclient.advertiser import Advertiser

class AdvertiserTestCase(unittest.TestCase):
    def test_get_advertisers(self):
        a = Advertiser(config.client_id, config.client_secret, config.refresh_token)
        a.refresh_access_token()

        advertisers = json.loads(a.traffic_types('advertisers', 92))

        print(advertisers)

        self.assertEqual(advertisers["response_code"], 200)
