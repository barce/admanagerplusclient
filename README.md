# admanagerplustclient
A python API client for Yahoo's Ad Manager Plus (formerly Brightroll Ad DSP)

# example
from admanagerplusclient import ampclient
brc = ampclient.BrightRollClient()
brc.cli_auth_dance()
brc.traffic_types('advertisers')
