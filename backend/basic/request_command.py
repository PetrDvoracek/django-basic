from .helper import check_time_format
import requests


class Command:
    def execute(self): pass

class GetFullTimeSerie(Command):
    url = "https://gateway.eu1.mindsphere.io/api/iottimeseries/v3/timeseries/"
    counter = 0

    def __init__(self, from_t, to_t, entity, serie_name, auth_token):
        self._from_time = from_t
        self._to_time = to_t
        self._entity = entity
        self._serie_name = serie_name
        self._auth_token = auth_token
        self._payload = ''
        self._headers = {
            'Authorization': self._auth_token,
            'cache-control': "no-cache",
            'Postman-Token': "325f46de-27d9-4a0b-a1f5-4bde202ab999",
            #        'Transfer-Encoding': 'chunked',
        }
        self._json_data = None
        self._url = "{0}{1}/{2}".format(self.url, self._entity, self._serie_name)

    @property
    def from_time(self):
        print("from time: {0}".format(self._from_time))
        return self._from_time

    @from_time.setter
    def from_time(self, from_t):
        check_time_format(from_t)
        return

    @property
    def to_time(self):
        print("to time: {0}".format(self._from_time))
        return self._to_time

    @to_time.setter
    def to_time(self, to_t):
        check_time_format(time=to_t)
        return

    @property
    def entity(self):
        return self._entity

    @property
    def serie_name(self):
        return self._serie_name

    #TODO DEBUG when release, comment it out!
    @property
    def auth_token(self):
        return self._auth_token

    def execute(self):
        GetFullTimeSerie.counter += 1
        response = requests.request("GET", self._url, data=self._payload, headers=self._headers, params=self._from_time)
        if response.status_code == 200:
            self._json_data = response.json()
            if response.links:
                next_url = response.links['next']['url']
                next_response = requests.request("GET", next_url, data=self._payload, headers=self._headers)
                #next_response = GetFullTimeSerie(from_t=from_t, to_t=self._to_time, entity=self._entity,
                #                                 serie_name=self.serie_name, auth_token=self._auth_token)
                #next_data = next_response.execute()
                next_data = next_response.json()
                self._json_data += next_data

        print(GetFullTimeSerie.counter)
        return self._json_data

# An object that holds commands:
class Macro:
    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def run(self):
        for c in self.commands:
            c.execute()


macro = Macro()

macro.run()