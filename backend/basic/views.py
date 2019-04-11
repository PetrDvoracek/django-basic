from django.shortcuts import render
import json
import numpy as np
import dateutil.parser
import datetime
from .request_command import *


def index(request):

    # get this from GUI!
    from_t = "2019-01-31T12:44:46.196Z"
    to_t = ""
    entity = '7f03ff1dc93941e69c09dfc63389d43e'
    serie_name = 'One'
    bearer_token = ''
    try:
        bearer_token = str(request.META['HTTP_AUTHORIZATION'])
    except:
        bearer_token="Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vdnNiZmVpMDEubG9jYWxob3N0OjgwODAvdWFhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktaWQtMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIxNzViMGYyYWZiMjM0MGEzODMyZGVhZTk0YjE3MDIwMiIsInN1YiI6IjYzNDdkMmFhLTRlMGQtNGY0MS04MDcxLTcwZTQ4ZWQwNTk4OSIsInNjb3BlIjpbImhlbGxvZGphbmdvLnNjb3BlIiwibWRzcDpjb3JlOmFnbS5mdWxsYWNjZXNzIiwibWRzcDpjb3JlOmFzc2V0bWFuYWdlbWVudC5hZG1pbiIsIm1kc3A6Y29yZTppb3QuZmlsQWRtaW4iLCJtZHNwOmNvcmU6aW90LmJ1bGtUaW1Vc2VyIiwibWRzcDpjb3JlOmlvdC5idWxrVGltQWRtaW4iLCJ1YWEub2ZmbGluZV90b2tlbiIsIm1kc3A6Y29yZTppb3QudGltQWRtaW4iLCJtZHNwOmNvcmU6aW90LnRpbVVzZXIiLCJtZHNwOmNvcmU6aW90LmZpbFVzZXIiXSwiY2xpZW50X2lkIjoiaGVsbG9kamFuZ28tdnNiZmVpMDEiLCJjaWQiOiJoZWxsb2RqYW5nby12c2JmZWkwMSIsImF6cCI6ImhlbGxvZGphbmdvLXZzYmZlaTAxIiwiZ3JhbnRfdHlwZSI6ImF1dGhvcml6YXRpb25fY29kZSIsInVzZXJfaWQiOiI2MzQ3ZDJhYS00ZTBkLTRmNDEtODA3MS03MGU0OGVkMDU5ODkiLCJvcmlnaW4iOiJ2c2JmZWkwMSIsInVzZXJfbmFtZSI6InBldHIuZHZvcmFjZWtAdnNiLmN6IiwiZW1haWwiOiJwZXRyLmR2b3JhY2VrQHZzYi5jeiIsImF1dGhfdGltZSI6MTU1NDk5NjgwMSwicmV2X3NpZyI6IjVlZTA4ZmJhIiwiaWF0IjoxNTU0OTk2ODAxLCJleHAiOjE1NTQ5OTg2MDEsImlzcyI6Imh0dHBzOi8vdnNiZmVpMDEucGlhbS5ldTEubWluZHNwaGVyZS5pby9vYXV0aC90b2tlbiIsInppZCI6InZzYmZlaTAxIiwiYXVkIjpbIm1kc3A6Y29yZTppb3QiLCJtZHNwOmNvcmU6YXNzZXRtYW5hZ2VtZW50IiwidWFhIiwiaGVsbG9kamFuZ28tdnNiZmVpMDEiLCJoZWxsb2RqYW5nbyIsIm1kc3A6Y29yZTphZ20iXSwidGVuIjoidnNiZmVpMDEiLCJzY2hlbWFzIjpbInVybjpzaWVtZW5zOm1pbmRzcGhlcmU6aWFtOnYxIl0sImNhdCI6InVzZXItdG9rZW46djEifQ.EGkIxcHcmgxI4_FsUqkSt1vboDnXQsMPzJAfsWistImmB0K-0PO98KParTcdk9SV-qjqnd03u-K27ug8msu5GxviK97oxtJGJDYbKwFgILhSyz4JPryii5MLs6836RUtT2xUidyOk2FmC2LNQZiWnKFgD630r8HhuAGGYGSkQFPlJllaDXPOvzM2Igt6UpYmYUzxbPO8jyszgEWYC0t1MVvsD4iqh8p2DQ7oYasH_8keo7hCdzeR46Pm9vB7Ta8EItHeh7i1BDhkaFB1H1oXpmfrhtH7ZKq5FS_DJ5bFv5NuBw7l96yDm_-yvt5YMnH627fTjONjgKge-u6ec1gTjw "

    request_com = GetFullTimeSerie(from_t, to_t, entity, serie_name, bearer_token)
    data = request_com.execute()
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

