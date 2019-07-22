
class Report:
    def create_report(self, reportOption, intervalTypeId, dateTypeId, startDate, endDate):
        headers = {'Content-Type': 'application/json', 'X-Auth-Method': 'OAUTH',
                   'X-Auth-Token': str(self.raw_token_results['access_token'])}
        payload = {"reportOption": reportOption, "intervalTypeId": intervalTypeId, "dateTypeId": dateTypeId,
                   "startDate": startDate, "endDate": endDate}
        print('--- payload ---')
        print(payload)
        print('--- payload ---')

        print('--- headers ---')
        print(headers)
        print('--- headers ---')

        r = requests.post(self.report_url, data=str(payload).replace("'", '"'), headers=headers)
        print(self.report_url)
        print(r)
        print(r.json())
        results = r.json()
        try:
            if results['errors']['httpStatusCode'] == 401:
                refresh_results_json = self.refresh_access_token()
        except:
            print("expected result")
        self.customerReportId = results['customerReportId']
        return r

    def extract_report(self):
        self.headers = {'Content-Type': 'application/json', 'X-Auth-Method': 'OAUTH',
                        'X-Auth-Token': str(self.raw_token_results['access_token'])}
        results = requests.get(self.report_url + self.customerReportId, headers=self.headers)
        self.curl_url = self.report_url + self.customerReportId
        self.debug_curl()

        r = results.json()
        try:
            if r['errors']['httpStatusCode'] == 401:
                refresh_results_json = self.refresh_access_token()
        except:
            print("expected result")
        print('--- extracted report json ---')
        print(r)
        print('--- extracted report json ---')
        try:
            self.report_results_url = r['url']
        except:
            self.report_results_url = ''

        try:
            validationMessages = r['validationMessages']
            if validationMessages[0]['message'] == 'Requests Per Minute (RPM) limit reached. Please try again later.':
                print('return rate limit message')
                return validationMessages[0]['message']

        except:
            print('no sleep')

        return self.report_results_url
