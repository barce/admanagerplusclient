import json

from admanagerplusclient.base import Base


class LineItem(Base):
    def get_lines_by_campaign_id(self, campaign_id, seat_id):
        endpoint = f"{self.dsp_host}/traffic/lines/"
        line_items = []
        params = {
            "orderId": campaign_id,
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
                for line_item in response.get('data').get('response'):
                    line_items.append(line_item)

            if int(len(line_items)) != int(expected_total):
                print('we have ' + str(len(line_items)))
                break

        response['data'] = line_items

        return json.dumps(response)

    def get_one(self, line_id, seat_id):
        url = f"{self.dsp_host}/traffic/lines/{str(line_id)}/"
        params = {
            "seatId": str(seat_id)
        }

        r = self.make_request(url, self.headers, 'GET', params=params)
        return r

    def create_one(self, data, seat_id):
        url = f"{self.dsp_host}/traffic/lines/"
        params = {
            "seatId": str(seat_id)
        }

        r = self.make_request(url, self.headers, 'POST', params=params, data=data)

        return r

    def update_one(self, lineitem_id, data, seat_id):
        url = f"{self.dsp_host}/traffic/lines/{str(lineitem_id)}/"
        params = {
            "seatId": str(seat_id)
        }

        r = self.make_request(url, self.headers, 'PUT', params=params, data=data)

        return r 

    def set_inventory_payload(self, dsp_lineitem_id):
        self.dsp_lineitem_id = dsp_lineitem_id

        self.inventory_payload = {
            "types": []
        }

    def set_deals(self, deal_ids):
        add_deal_ids = []
        for id in deal_ids:
            add_deal_ids.append(int(id))

        self.inventory_payload["deals"] = {
            # "removed": [],
            "clearAll": False,
            "added": add_deal_ids
        }
        self.inventory_payload["types"].append(
            {
                "name": "EXCHANGES",
                "isTargeted": True
            }
        )

    def set_exchanges(self, exchange_ids):
        add_exchange_ids = []
        for id in exchange_ids:
            add_exchange_ids.append(int(id))

        self.inventory_payload["publishers"] = add_exchange_ids
        self.inventory_payload["publishersIncluded"] = True
        self.inventory_payload["types"].append(
            {
                "name": "EXCHANGES",
                "isTargeted": True
            }
        )

    def create_sitelist(self, advertiser_id, seat_id, name, list_type, list):
            app_domain_data = []
            for item in list:
                app_domain_data.append({"itemName": str(item)})

            payload = {
                "accountId": advertiser_id,
                "name": name,
                "status": "ACTIVE",
                "type": list_type,
                "items": app_domain_data
            }

            url = self.dsp_host + "/traffic/sitelists/?seatId={0}".format(seat_id)
            r = self.make_request(url, self.headers, 'POST', data=payload)
            return r

    def update_sitelist(self, id, advertiser_id, seat_id, name, list_type, list):
        app_domain_data = []
        for item in list:
            app_domain_data.append({"itemName": str(item)})

        payload = {
            "accountId": advertiser_id,
            "name": name,
            "status": "ACTIVE",
            "type": list_type,
            "items": app_domain_data
        }

        url = self.dsp_host + "/traffic/sitelists/" + str(id) + "?seatId={0}".format(seat_id)
        r = self.make_request(url, self.headers, 'PUT', data=payload)
        return r

    def set_sitelists(self, add_site_list_ids, remove_site_list_ids=[]):
        site_list_data = []
        for id in add_site_list_ids:
            rval = {
                "excluded": False,
                "entityId": int(id)
            }
            site_list_data.append(rval)

        self.inventory_payload["siteLists"] = {
            "removed": remove_site_list_ids,
            "clearAll": False,
            "added": site_list_data
        }
        self.inventory_payload["types"].append(
            {
                "name": "SITE_LISTS",
                "isTargeted": True
            }
        )

    def update_inventory(self, seat_id):
        url = self.dsp_host + "/traffic/lines/{0}/targeting?seatId={1}".format(int(self.dsp_lineitem_id), seat_id)
        r = self.make_request(url, self.headers, 'POST', data=self.inventory_payload)
        return r
