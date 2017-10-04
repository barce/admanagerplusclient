#!/usr/bin/env python


# 20500

from admanagerplusclient import ampclient

brc = ampclient.BrightRollClient()

brc.refresh_access_token()

# advertisers = brc.traffic_type_by_id('advertisers', 20500)
# print('--- advertisers ---')
# print(advertisers)
# 
# print('--- campaign by id ---')
# campaigns = brc.traffic_type_by_id('campaigns', 44582)
# print(campaigns)
# 
# print('--- campaign by query string id ---')
# campaigns = brc.traffic_types('campaigns?accountId=20500')
# print(campaigns)

# print('--- campaign traffic types by filter ---')
# campaigns = brc.traffic_types_by_filter('campaigns', 20500)
# print(campaigns)
# 
# print('--- line by filter ---')
# lines = brc.traffic_types_by_filter('lines', 44582)
# print(lines)
# print('--- lines by query string orderId ---')
# lines = brc.traffic_types('lines?orderId=44582')
# print(lines)


# print('--- deals by query string id ---')
# deals = brc.traffic_types('deals?accountId=20500')
# print(deals)

reportOptions = { "timezone": "America/New_York", "currency": 4, "dimensionTypeIds": [ 1,3,4,5,6,8,9,34,50,63 ], "metricTypeIds": [ 1,2,23,25,29,44,46,100,101,116,117,129,166,167 ] }

stuff = brc.create_report(reportOptions, 2, 4, '2016-09-01T00:00:00-05:00','2016-09-14T00:00:00-05:00')
print('--- create_report ---')
print(stuff)

