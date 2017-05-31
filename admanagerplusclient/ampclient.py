#!/usr/bin/env python

from future.standard_library import install_aliases
install_aliases()


import json
import jwt
import requests
import time
import os


use_environment_variables = None

try:
    from django.conf import settings
except ImportError:
    use_environment_variables = True


class BrightRollClient:
  client_id = None
  client_secret = None
  api_key = None
  id_host = None
  one_host = None
  aud = None
  payload = None
  encoded_payload = None
  oauth_url = None
  payload_url = None
  headers = None
  authorized_headers = None
  token = None


  def __init__(self):
    self.client_id = os.environ['BR_CLIENT_ID']
    self.client_secret = os.environ['BR_CLIENT_SECRET']
    self.api_key = os.environ['BR_API_KEY']
    self.id_host = os.environ['BR_ID_HOST']
    self.one_host = os.environ['BR_ONE_HOST']


  def campaigns(self):
    return True

  def deals(self):
    return True
