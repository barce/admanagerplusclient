#!/usr/bin/env python

import json
import requests

from admanagerplusclient.connection import Connection


class Base:

    def __init__(self, connection):
        
        self.connection = connection

        self.dsp_host = "https://dspapi.admanagerplus.yahoo.com"
        self.report_url = 'https://api-sched-v3.admanagerplus.yahoo.com/yamplus_api/extreport/'

        self.headers = {
            'Content-Type': 'application/json',
            'X-Auth-Method': 'OAUTH',
            'X-Auth-Token': str(self.connection.token)
        }

    #
    #
    # traffic types
    #
    #

    def generate_json_response(self, r, results_json, request_body):
        response_json = {
            'request_body': self.curl_command
        }

        if results_json['errors'] is not None:
            response_json['msg_type'] = 'error'
            response_json['msg'] = results_json['errors']
            response_json['data'] = results_json['errors']
            response_json['response_code'] = results_json['errors']['httpStatusCode']

        else:
            response_json['msg_type'] = 'success'
            # display the error message that comes back from request
            response_json['msg'] = ''
            response_json['data'] = results_json
            response_json['response_code'] = r.status_code

        return response_json

        # make_request(method_type) --> pass in method_type

    def make_request(self, url, headers, method_type, data=None):
        request_body = url, headers, data
        r, results_json = self.make_new_request(url, self.connection.token, method_type, headers, data)

        if results_json['errors'] is not None:
            if results_json['errors']['httpStatusCode'] in [400, 401]:
                # refresh access token
                self.token = self.refresh_access_token()['access_token']
                # apply headers with new token, return response and response dict
                r, results_json = self.make_new_request(url, self.token, method_type, headers, data)

        # use results_json to create updated json dict
        response_json = self.generate_json_response(r, results_json, request_body)

        return json.dumps(response_json)

    def make_new_request(self, url, token, method_type, headers, data=None):
        #print ("URL")
        #print (url)
        #print ("DATA")
        #print (data)

        # modify headers with new access token
        self.headers['X-Auth-Token'] = token

        if method_type == 'GET':
            r = requests.get(url, headers=self.headers)
        if method_type == 'POST':
            r = requests.post(url, headers=self.headers, verify=False, data=json.dumps(data))
        if method_type == 'PUT':
            r = requests.put(url, headers=self.headers, verify=False, data=json.dumps(data))
        results_json = r.json()

        #print ("results_json")
        #print (results_json)
        command = "curl -v -H {headers} {data} -X {method} {uri}"
        header_list = ['"{0}: {1}"'.format(k, v) for k, v in headers.items()]
        header = " -H ".join(header_list)
        self.curl_command = command.format(method=method_type, headers=header, data=data, uri=url)
        """
        print ("===========================")
        print ("")
        print (command.format(method=method_type, headers=header, data=data, uri=url))
        print ("")
        print ("")
        print ("================================")
        """

        return r, results_json

    def traffic_types(self, s_type, seat_id=None):
        url = self.dsp_host + "/traffic/" + str(s_type)
        if seat_id is not None:
            url += "/?seatId=" + str(seat_id)

        r = self.make_request(url, self.headers, 'GET')
        return r

    # Works for s_types:
    # advertisers, campaigns, lines
    def traffic_type_by_id(self, s_type, cid, seat_id):
        url = self.dsp_host + "/traffic/" + str(s_type)
        url = url + "/" + str(cid) + "/?seatId=" + str(seat_id)
        # self.curl_url = url
        # self.debug_curl()

        r = self.make_request(url, self.headers, 'GET')
        return r

    # TODO:
    # do not pass to the results string if not set on our end
    def traffic_types_by_filter(self, s_type, account_id, page=0, limit=0, sort='', direction='asc', query=''):
        url = self.dsp_host + "/traffic/" + str(s_type)
        if s_type == 'lines':
            url = url + "?orderId=" + str(account_id)
        else:
            url = url + "?accountId=" + str(account_id)

        if page > 0:
            url = url + "&page=" + str(page)
        if limit > 0:
            url = url + "&limit=" + str(limit)
        if sort != '':
            url = url + "&sort=" + str(sort)
        if query != '':
            url = url + "&query=" + str(query)
        url = url + "&dir=" + str(direction)

        r = self.make_request(url, self.headers, 'GET')
        r = json.loads(r)
        r['data']['response'] = r['data']['response'][0]
        r = json.dumps(r)
        return r

    def update_traffic_type(self, s_type, cid, payload, seat_id):
        url = self.dsp_host + "/traffic/" + str(s_type) + "/" + str(cid) + "/?seatId=" + str(seat_id)
        r = self.make_request(url, self.headers, 'PUT', payload)
        return r

    def create_traffic_type(self, s_type, payload, seat_id):
        url = self.dsp_host + "/traffic/" + str(s_type) + "/?seatId=" + str(seat_id)
        r = self.make_request(url, self.headers, 'POST', payload)
        return r
