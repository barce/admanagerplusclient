from admanagerplusclient.base import Base


class Creative(Base):
    def get_creatives_by_lineitem(self, lineitem_id, seat_id):
        url = f"{self.dsp_host}/traffic/ads"
        url += f"/?lineId={lineitem_id}&seatId={str(seat_id)}"

        r = self.make_request(url, self.headers, 'GET')
        return r

    def get_one(self, creative_id, seat_id):
        url = f"{self.dsp_host}/traffic/ads/{str(creative_id)}"
        url += "/?seatId=" + str(seat_id)

        r = self.make_request(url, self.headers, 'GET')
        return r
