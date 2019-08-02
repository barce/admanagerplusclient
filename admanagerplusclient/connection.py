import requests
import base64

class Connection:
    
    def __init__(self, client_id, client_secret, refresh_token):
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token

        self.id_host = "https://api.login.yahoo.com"

        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': "Basic " + self.base64auth().decode('utf-8'),
            'X-Auth-Token': None
        }

        self.refresh_access_token()

    def refresh_access_token(self):
        get_token_url = self.id_host + "/oauth2/get_token"
        payload = {
            "grant_type": "refresh_token",
            "redirect_uri": "oob",
            "refresh_token": self.refresh_token.encode('utf-8')
        }

        r = requests.post(get_token_url, data=payload, headers=self.headers, verify=False) # CHANGE THIS BACK AFTER TESTING
        results_json = r.json()
        try:
            self.token = results_json['access_token']
        except:
            pass

        return results_json

    def base64auth(self):
        return base64.b64encode((self.client_id + ":" + self.client_secret).encode())
