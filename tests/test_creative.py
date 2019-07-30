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

        creatives = json.loads(c.get_creatives_by_lineitem(376875, 92))
        print(creatives)

        self.assertEqual(creatives["response_code"], 200)

    def test_get_one_creative(self):
        c = Creative(CreativeTestCase.connection)

        creative = json.loads(c.get_one(1977315, 92))
        print(creative)

        self.assertEqual(creative["response_code"], 200)
