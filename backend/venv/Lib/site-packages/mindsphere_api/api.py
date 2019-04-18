import requests
import urllib.parse as urlparse
import json

def GetFullTimeSeries(from_t, to_t, entity, serie_name, auth_token, data=[]):
    base_url = "https://gateway.eu1.mindsphere.io/api/iottimeseries/v3/timeseries/"
    url = "{0}{1}/{2}".format(base_url, entity, serie_name)
    payload = ''
    params = {"from":from_t}
    if to_t:
        params.update({"to" : to_t})
    headers = {
        'Authorization': auth_token,
        'cache-control': "no-cache",
        'Postman-Token': "325f46de-27d9-4a0b-a1f5-4bde202ab999",
        #        'Transfer-Encoding': 'chunked',
    }
    response = requests.request("GET", url, data=payload, headers=headers, params=params)
    if response.status_code == 200:
        data.extend(response.json())
        if response.links:
            next_url = response.links['next']['url']
            if 'from' in next_url:
                parsed_url = urlparse.urlparse(next_url)
                from_t = urlparse.parse_qs(parsed_url.query)['from'][0]
                next_data = GetFullTimeSeries(from_t=from_t, to_t=to_t, entity=entity,
                                                serie_name=serie_name, auth_token=auth_token)
                data.extend(next_data)
            else:
                raise Exception("next_url does not contains 'from' parameter: {0}".format(next_url))
    return data


if __name__=='__main__':
    print(len(GetFullTimeSeries(from_t="2019-01-31T12:44:46.196Z",to_t='', entity='7f03ff1dc93941e69c09dfc63389d43e', serie_name='One',
                      auth_token="")))
