from django.shortcuts import render
import json
import numpy as np
import dateutil.parser
import datetime
#from .request_command import *
#from . import api


def index(request):

    # get this from GUI!
    from_t = "2019-01-31T12:44:46.196Z"
    to_t = "2019-01-31T12:44:46.196Z"
    entity = '7f03ff1dc93941e69c09dfc63389d43e'
    serie_name = 'One'
    bearer_token = ''
    try:
        bearer_token = str(request.META['HTTP_AUTHORIZATION'])
    except:
        bearer_token="Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vdnNiZmVpMDEubG9jYWxob3N0OjgwODAvdWFhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktaWQtMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIwZjM2MzQ2MjQ0M2Q0MzRlOTNlYTYyZWQxMjNhZTkwNyIsInN1YiI6IjYzNDdkMmFhLTRlMGQtNGY0MS04MDcxLTcwZTQ4ZWQwNTk4OSIsInNjb3BlIjpbImhlbGxvZGphbmdvLnNjb3BlIiwibWRzcDpjb3JlOmFnbS5mdWxsYWNjZXNzIiwibWRzcDpjb3JlOmFzc2V0bWFuYWdlbWVudC5hZG1pbiIsIm1kc3A6Y29yZTppb3QuZmlsQWRtaW4iLCJtZHNwOmNvcmU6aW90LmJ1bGtUaW1Vc2VyIiwibWRzcDpjb3JlOmlvdC5idWxrVGltQWRtaW4iLCJ1YWEub2ZmbGluZV90b2tlbiIsIm1kc3A6Y29yZTppb3QudGltQWRtaW4iLCJtZHNwOmNvcmU6aW90LnRpbVVzZXIiLCJtZHNwOmNvcmU6aW90LmZpbFVzZXIiXSwiY2xpZW50X2lkIjoiaGVsbG9kamFuZ28tdnNiZmVpMDEiLCJjaWQiOiJoZWxsb2RqYW5nby12c2JmZWkwMSIsImF6cCI6ImhlbGxvZGphbmdvLXZzYmZlaTAxIiwiZ3JhbnRfdHlwZSI6ImF1dGhvcml6YXRpb25fY29kZSIsInVzZXJfaWQiOiI2MzQ3ZDJhYS00ZTBkLTRmNDEtODA3MS03MGU0OGVkMDU5ODkiLCJvcmlnaW4iOiJ2c2JmZWkwMSIsInVzZXJfbmFtZSI6InBldHIuZHZvcmFjZWtAdnNiLmN6IiwiZW1haWwiOiJwZXRyLmR2b3JhY2VrQHZzYi5jeiIsImF1dGhfdGltZSI6MTU1NDg4ODU4NSwicmV2X3NpZyI6IjVlZTA4ZmJhIiwiaWF0IjoxNTU0ODg4NTg1LCJleHAiOjE1NTQ4OTAzODUsImlzcyI6Imh0dHBzOi8vdnNiZmVpMDEucGlhbS5ldTEubWluZHNwaGVyZS5pby9vYXV0aC90b2tlbiIsInppZCI6InZzYmZlaTAxIiwiYXVkIjpbIm1kc3A6Y29yZTppb3QiLCJtZHNwOmNvcmU6YXNzZXRtYW5hZ2VtZW50IiwidWFhIiwiaGVsbG9kamFuZ28tdnNiZmVpMDEiLCJoZWxsb2RqYW5nbyIsIm1kc3A6Y29yZTphZ20iXSwidGVuIjoidnNiZmVpMDEiLCJzY2hlbWFzIjpbInVybjpzaWVtZW5zOm1pbmRzcGhlcmU6aWFtOnYxIl0sImNhdCI6InVzZXItdG9rZW46djEifQ.RZvvfxGAX-OfRvI9XHhfmYIiywzA58SoVxdYpFxU_e7DvG136uUG-UR-0oWadS4YIiYgN8puYOKo2B4lw8QPC6H_K0t1OzC0Gt2Kpmb2MFN6Wb3jFNBAi4ZZXTPefVbTyACyj1_kizzi9ToxuIqbgYItb8wVNwlP_dFdnT2maxGc6ln1QqMnHSqy3gGlqRh4av-k9nOWdMIUp5vbJZZA6Pbabxb-L6vohw_72SeRnSd_oOpZ2aej-gNqFvLLtGfIKEpn4kVxTeremlX_YTighM1WbQ5vMjQtzl9Ufm9Kdlb7mb7dq_YLSnPVP7_Vj4-VNr2z0XDww6xOsD0bY6iQ0w"

    data = GetFullTimeSeries(from_t, to_t, entity, serie_name, bearer_token)

    try:
        x_data=[]
        y_data=[]
        for x in data:
            if 'One' in x.keys():
                x_data.append(x['_time'])
                y_data.append(x['One'])
            else:
                print(x)
    except Exception as e:
        pass

    return render(request, 'index_ojan.html', {'json_x':x_data, 'json_y':y_data, 'stuff' : bearer_token})

def get_time_serie(request):
    pass

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
