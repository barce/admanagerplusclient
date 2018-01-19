#!/usr/bin/env python


# 20500
import time
import json

from admanagerplusclient import ampclient

brc = ampclient.BrightRollClient()

brc.refresh_access_token()

# test for edits

campaign = brc.traffic_type_by_id('campaigns', 86184)
print(campaign)

print('change status')
print('OLD status:')
print(campaign['response']['status'])
print('NEW status:')
print('PAUSED')
print('running update with complete object...')
resp = brc.update_traffic_type('campaigns', 86184, json.dumps(campaign['response']))

print('fetching updated campaign...')
campaign = brc.traffic_type_by_id('campaigns', 86184)
print(campaign)

print('running update with just one column changed...')
resp = brc.update_traffic_type('campaigns', 86184, json.dumps({"status": "PAUSED"}))
print('fetching updated campaign...')
campaign = brc.traffic_type_by_id('campaigns', 86184)
print(campaign)

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

# EXIT
exit()

# -d '{"reportOption": {"timezone": "America/New_York", "dimensionTypeIds": [1, 3, 4, 5, 6, 8, 9, 34, 50, 63], "metricTypeIds": [1, 2, 23, 25, 29, 44, 46, 100, 101, 116, 117, 129, 166, 167], "currency": 4}, "intervalTypeId": 1, "startDate": "2017-09-18T00:00:00-05:00", "endDate": "2017-09-18T11:59:59-05:00", "dateTypeId": 11}'



# REPORT PARAMS from RYAN
# reportOptions = { "timezone": "America/New_York", "currency": 4, "dimensionTypeIds": [ 1,3,4,5,6,8,9,34,50,63 ], "metricTypeIds": [ 1,2,23,25,29,44,46,100,101,116,117,129,166,167 ] }

# REPORT PARAMS for TEST
reportOptions = {"timezone": "America/New_York", "dimensionTypeIds": [1, 3, 4, 5, 6, 8, 9, 34, 50, 63], "metricTypeIds": [1, 2, 23, 25, 29, 44, 46, 100, 101, 116, 117, 129, 166, 167], "currency": 4}

# create_report(reportOptions, intervalTypeId, dateTypeId, start_date, stop_date)

# ryan's params
# stuff = brc.create_report(reportOptions, 2, 4, '2016-09-01T00:00:00-05:00','2016-09-14T00:00:00-05:00')

# test params
stuff = brc.create_report(reportOptions, 1, 11, '2017-10-05T00:00:00-05:00','2017-10-05T11:59:59-05:00')


print('--- create_report ---')
print(stuff)

# results to parse:
# {"customerReportId":"e435447d-1e6b-4004-9e79-92be4e39d737","status":"Success","url":"https://s.yimg.com/ff/pbp/ext_report/extrep4767039211623876287.csv","requestPayload":"{\"reportOption\":{\"timezone\":\"America/New_York\",\"dimensionTypeIds\":[1,3,4,5,6,8,9,34,50,63],\"metricTypeIds\":[1,2,23,25,29,44,46,100,101,116,117,129,166,167],\"currency\":4},\"intervalTypeId\":1,\"startDate\":\"2017-09-18T00:00:00-05:00\",\"endDate\":\"2017-09-18T11:59:59-05:00\",\"dateTypeId\":11}","jobStartDate":"2017-10-05T16:58:38.000-07:00","jobEndDate":"2017-10-05T17:00:33.000-07:00","numRows":451347}

x = 0
while (x == 0):
    report_url = brc.extract_report()
    print(report_url)
    s_input = raw_input('Enter your input:')


