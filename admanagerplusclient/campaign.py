from admanagerplusclient.base import Base


class Campaign(Base):
    def get_all_by_advertiser(self, advertiser_id, seat_id):
        url = f"{self.dsp_host}/traffic/campaigns"
        url += f"/?accountId={advertiser_id}&seatId={str(seat_id)}"

        r = self.make_request(url, self.headers, 'GET')
        return r

    def get_one(self, campaign_id, seat_id):
        url = f"{self.dsp_host}/traffic/campaigns/{str(campaign_id)}"
        url += "/?seatId=" + str(seat_id)

        r = self.make_request(url, self.headers, 'GET')
        return r
