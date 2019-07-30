import config
import json

import unittest

from admanagerplusclient.connection import Connection
from admanagerplusclient.creative import Creative

class CreativeTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = Connection(config.client_id, config.client_secret, config.refresh_token)

    def test_get_creatives_by_lineitem(self):
        c = Creative(CreativeTestCase.connection)

        creatives = json.loads(c.get_creatives_by_lineitem(97893, 92))
        print(lines)

        self.assertEqual(lines["response_code"], 200)

    def test_get_one_creative(self):
        c = Creative(CreativeTestCase.connection)

        creative = json.loads(c.get_one(376875, 92))
        print(creative)

        self.assertEqual(line["response_code"], 200)
