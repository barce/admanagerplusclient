
class LineItem:
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
        headers = {'Content-Type': 'application/json', 'X-Auth-Method': 'OAUTH', 'X-Auth-Token': str(self.token)}
        url = self.dsp_host + "/traffic/lines/{0}/targeting?seatId={1}".format(int(self.dsp_lineitem_id), seat_id)
        r = self.make_request(url, headers, 'POST', self.inventory_payload)
        return r
