import json
from admanagerplusclient.base import Base


class Campaign(Base):
    def get_all_by_advertiser(self, advertiser_id, seat_id):
        endpoint = f"{self.dsp_host}/traffic/campaigns/"
        campaigns = []
        params = {
            "accountId": advertiser_id,
            "seatId": str(seat_id),
            "limit": 100,
            "page": 0
        }

        while True:
            params["page"] += 1
            expected_total = params["page"] * params["limit"]

            response = json.loads(self.make_request(endpoint, self.headers, 'GET', params=params))

            if response.get('msg_type') == "error":
                for error in response.get('data').get('validationErrors'):
                    if error.get('propertyName') == "TRAFFIC_LIMIT_PER_MIN":
                        print("")
                        print("")
                        print("")
                        print("Traffic Limit Exceeded Sleeping...")
                        time.sleep(61)
                        print("")
                        print("")
                        print("")

                        response = json.loads(self.make_request(endpoint, self.headers, 'GET', params=params))

            if response.get('msg_type') == "success":
                for campaign in response.get('data').get('response'):
                    campaigns.append(campaign)

            if int(len(campaigns)) != int(expected_total):
                print('we have ' + str(len(campaigns)))
                break

        response['data'] = campaigns

        return json.dumps(response)

    def get_one(self, campaign_id, seat_id):
        url = f"{self.dsp_host}/traffic/campaigns/{str(campaign_id)}/"
        params = {
            "seatId": str(seat_id)
        }

        r = self.make_request(url, self.headers, 'GET', params=params)
        return r

    def create_one(self, data, seat_id):
        url = f"{self.dsp_host}/traffic/campaigns/"
        params = {
            "seatId": str(seat_id)
        }

        r = self.make_request(url, self.headers, 'POST', params=params, data=data)

        return r

    def update_one(self, campaign_id, data, seat_id):
        url = f"{self.dsp_host}/traffic/campaigns/{str(campaign_id)}/"
        params = {
            "seatId": str(seat_id)
        }

        r = self.make_request(url, self.headers, 'PUT', params=params, data=data)

        return r
