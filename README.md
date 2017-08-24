# admanagerplustclient
A python API client for Yahoo's Ad Manager Plus (formerly Brightroll Ad DSP)

# example for 1st time use

from admanagerplusclient import ampclient

brc = ampclient.BrightRollClient()

brc.cli_auth_dance()

brc.traffic_types('advertisers')

# example for ETC or nightly job server
from admanagerplusclient import ampclient

brc = ampclient.BrightRollClient()

brc.refresh_access_token()

brc.traffic_types('advertisers')

