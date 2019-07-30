from admanagerplusclient.base import Base


class Creative(Base):
    def get_creatives_by_lineitem(self, lineitem_id, seat_id):
        url = f"{self.dsp_host}/traffic/lines"
        url += f"/?orderId={campaign_id}&seatId={str(seat_id)}"

        r = self.make_request(url, self.headers, 'GET')
        return r

    def get_one(self, line_id, seat_id):
        url = f"{self.dsp_host}/traffic/lines/{str(line_id)}"
        url += "/?seatId=" + str(seat_id)

        r = self.make_request(url, self.headers, 'GET')
        return r
