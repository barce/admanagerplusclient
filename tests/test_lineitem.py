import config
import json

import unittest

from admanagerplusclient.connection import Connection
from admanagerplusclient.lineitem import LineItem

class LineItemTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = Connection(config.client_id, config.client_secret, config.refresh_token)

    def test_get_all_lines_by_campaign(self):
        l = LineItem(LineItemTestCase.connection)

        lines = json.loads(l.get_lines_by_campaign_id(97893, 92))
        print(lines)

        self.assertEqual(lines["response_code"], 200)

    def test_get_one_lineitem(self):
        l = LineItem(LineItemTestCase.connection)

        line = json.loads(l.get_one(376875, 92))
        print(line)

        self.assertEqual(line["response_code"], 200)
