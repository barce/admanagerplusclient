import json

from admanagerplusclient.base import Base


class Deal(Base):

    def get_all(self, seat_id):
        deals = []
        added = {}
        page = 0
        limit = 100

        while True:
            page += 1
            expected_total = page * limit
            endpoint = f"{self.dsp_host}/traffic/deals"
            params = {
                "page": page,
                "limit": limit,
                "seatId": seat_id
            }

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
                for deal in response.get('data').get('response'):
                    deal_id = deal.get('exchangeDealId')
                    push_id = deal.get('id')

                    if added.get(push_id) is None:
                        added[push_id] = deal_id
                        deals.append(deal)

            if int(len(deals)) != int(expected_total):
                print('we have ' + str(len(deals)))
                break

        response['data'] = deals

        return json.dumps(response)
