import config
import json

import unittest

from admanagerplusclient.connection import Connection
from admanagerplusclient.deal import Deal

class DealTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = Connection(config.client_id, config.client_secret, config.refresh_token)

    def test_get_all_deals_by_seat(self):
        d = Deal(DealTestCase.connection)

        deals = json.loads(d.get_all(92))
        print(deals)

        self.assertEqual(deals["response_code"], 200)
