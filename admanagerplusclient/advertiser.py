from admanagerplusclient.base import Base


class Advertiser(Base):
    
    def get_all(self, seat_id):
        url = f"{self.dsp_host}/traffic/advertisers"
        params = {
            "seatId": str(seat_id)
        }

        r = self.make_request(url, self.headers, 'GET', params=params)
        return r

    def get_one(self, advertiser_id, seat_id):
        url = f"{self.dsp_host}/traffic/advertisers/{str(advertiser_id)}"
        params = {
            "seatId": str(seat_id)
        }

        r = self.make_request(url, self.headers, 'GET', params=params)
        return r
