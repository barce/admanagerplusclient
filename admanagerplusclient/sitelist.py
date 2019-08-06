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
            r = self.make_request(url, self.headers, 'POST', payload)
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
        r = self.make_request(url, self.headers, 'PUT', payload)
        return r