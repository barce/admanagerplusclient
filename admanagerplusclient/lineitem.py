from admanagerplusclient.base import Base


class LineItem(Base):
    def get_lines_by_campaign_id(self, campaign_id, seat_id):
        url = f"{self.dsp_host}/traffic/lines"
        url += f"/?orderId={campaign_id}&seatId={str(seat_id)}"

        r = self.make_request(url, self.headers, 'GET')
        return r

    def get_one(self, line_id, seat_id):
        url = f"{self.dsp_host}/traffic/lines/{str(line_id)}"
        url += "/?seatId=" + str(seat_id)

        r = self.make_request(url, self.headers, 'GET')
        return r

    def set_inventory_payload(self, dsp_lineitem_id):
        self.dsp_lineitem_id = dsp_lineitem_id

        self.inventory_payload = {
            "types": []
        }

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

    def update_inventory(self, seat_id):
        url = self.dsp_host + "/traffic/lines/{0}/targeting?seatId={1}".format(int(self.dsp_lineitem_id), seat_id)
        r = self.make_request(url, self.headers, 'POST', self.inventory_payload)
        return r
