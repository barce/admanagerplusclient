import config
import json

import unittest

from admanagerplusclient.connection import Connection
from admanagerplusclient.advertiser import Advertiser

class AdvertiserTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = Connection(config.client_id, config.client_secret, config.refresh_token)

    def test_get_all_advertisers(self):
        c = AdvertiserTestCase.connection
        a = Advertiser(c)

        advertisers = json.loads(a.get_all(92))
        print(advertisers)
        self.assertEqual(advertisers["response_code"], 200)

    def test_get_one_advertiser(self):
        c = AdvertiserTestCase.connection
        a = Advertiser(c)

        advertiser = json.loads(a.get_one(25063, 92))

        print(advertiser)

        self.assertEqual(advertiser["response_code"], 200)
        self.assertEqual(advertiser["data"]["response"]["name"], "Hawaii Tourism")
