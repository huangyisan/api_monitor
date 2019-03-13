import requests
import base64

class Ambari(object):
    def __init__(self, platform, url, username, password, querystring):
        self.platform = platform
        self.url = url + platform
        self.username = username
        self.passpword = password
        self.querystring = querystring

    def _base64(self):
        s = '{username}:{password}'.format(username=self.username,password=self.passpword)
        s = s.encode()
        return base64.b64encode(s)

    def get_response(self):
        _base64 = self._base64()
        _base64 = _base64.decode()
        headers = {
            'cache-control': "no-cache",
            'authorization': "Basic {0}".format(_base64)
        }

        querystring = self.querystring
        response = requests.request("GET", url=self.url, headers=headers, params=querystring)
        return response.json()

    def get_alerts_summary(self):
        response_json = self.get_response()
        info_dict = response_json.get("alerts_summary_hosts")
        # print(info_dict)
        return info_dict







