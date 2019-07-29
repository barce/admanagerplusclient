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

    def generate_json_response(self, r, results_json, data=None):
        response_json = {
            'request_body': self.generate_curl_command(r.request.method, r.url, self.headers, data)
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


    # wraps around make_new_request to test that the token is valid
    def make_request(self, url, headers, method_type, data=None):
        # request_body = url, headers, data
        r = self.make_new_request(url, self.connection.token, method_type, headers, data)
        results_json = r.json()

        if results_json['errors'] is not None:
            if results_json['errors']['httpStatusCode'] in [400, 401]:
                self.connection.token = self.refresh_access_token()['access_token']
                r = self.make_new_request(url, self.connection.token, method_type, headers, data)

        # use results_json to create updated json dict
        response_json = self.generate_json_response(r, results_json, data)

        return json.dumps(response_json)

    def make_new_request(self, url, token, method_type, headers, data=None):

        # modify headers with new access token
        self.headers['X-Auth-Token'] = token

        if method_type == 'GET':
            r = requests.get(url, headers=self.headers)
        if method_type == 'POST':
            r = requests.post(url, headers=self.headers, verify=False, data=json.dumps(data))
        if method_type == 'PUT':
            r = requests.put(url, headers=self.headers, verify=False, data=json.dumps(data))
        results_json = r.json()

        return r

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

    def generate_curl_command(self, method, url, headers, data=None):
        command = "curl -v -H {headers} {data} -X {method} {uri}"
        
        header_list = ['"{0}: {1}"'.format(k, v) for k, v in headers.items()]
        header = " -H ".join(header_list)

        return command.format(method=method, headers=header, data=data, uri=url)
