import json

from admanagerplusclient.base import Base


class SiteList(Base):
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
