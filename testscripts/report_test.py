#!/usr/bin/env python


# 20500
import time
import json

from admanagerplusclient import ampclient

brc = ampclient.BrightRollClient()

brc.refresh_access_token()


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


