from django.shortcuts import render
import json
import numpy as np
import dateutil.parser
import datetime
from .request_command import *


def index(request):

    url = "https://gateway.eu1.mindsphere.io/api/iottimeseries/v3/timeseries/"
    
    from_t = {"from":"2019-01-31T12:44:46.196Z"}
    to_t = {"to":""}
    entity = '7f03ff1dc93941e69c09dfc63389d43e'
    serie_name = 'One'
    bearer_token = ''
    try:
        bearer_token = str(request.META['HTTP_AUTHORIZATION'])
    except:
        bearer_token="Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vdnNiZmVpMDEubG9jYWxob3N0OjgwODAvdWFhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktaWQtMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1NjY2ZThkMWUwMWM0NjQ2OTdlNjJjZmJlODU5OTIxMSIsInN1YiI6IjYzNDdkMmFhLTRlMGQtNGY0MS04MDcxLTcwZTQ4ZWQwNTk4OSIsInNjb3BlIjpbImhlbGxvZGphbmdvLnNjb3BlIiwibWRzcDpjb3JlOmFnbS5mdWxsYWNjZXNzIiwibWRzcDpjb3JlOmFzc2V0bWFuYWdlbWVudC5hZG1pbiIsIm1kc3A6Y29yZTppb3QuZmlsQWRtaW4iLCJtZHNwOmNvcmU6aW90LmJ1bGtUaW1Vc2VyIiwibWRzcDpjb3JlOmlvdC5idWxrVGltQWRtaW4iLCJ1YWEub2ZmbGluZV90b2tlbiIsIm1kc3A6Y29yZTppb3QudGltQWRtaW4iLCJtZHNwOmNvcmU6aW90LnRpbVVzZXIiLCJtZHNwOmNvcmU6aW90LmZpbFVzZXIiXSwiY2xpZW50X2lkIjoiaGVsbG9kamFuZ28tdnNiZmVpMDEiLCJjaWQiOiJoZWxsb2RqYW5nby12c2JmZWkwMSIsImF6cCI6ImhlbGxvZGphbmdvLXZzYmZlaTAxIiwiZ3JhbnRfdHlwZSI6ImF1dGhvcml6YXRpb25fY29kZSIsInVzZXJfaWQiOiI2MzQ3ZDJhYS00ZTBkLTRmNDEtODA3MS03MGU0OGVkMDU5ODkiLCJvcmlnaW4iOiJ2c2JmZWkwMSIsInVzZXJfbmFtZSI6InBldHIuZHZvcmFjZWtAdnNiLmN6IiwiZW1haWwiOiJwZXRyLmR2b3JhY2VrQHZzYi5jeiIsImF1dGhfdGltZSI6MTU1MzI0NzkyNCwicmV2X3NpZyI6Ijg2MzcxMGQ4IiwiaWF0IjoxNTUzMjQ3OTI1LCJleHAiOjE1NTMyNDk3MjUsImlzcyI6Imh0dHBzOi8vdnNiZmVpMDEucGlhbS5ldTEubWluZHNwaGVyZS5pby9vYXV0aC90b2tlbiIsInppZCI6InZzYmZlaTAxIiwiYXVkIjpbIm1kc3A6Y29yZTppb3QiLCJtZHNwOmNvcmU6YXNzZXRtYW5hZ2VtZW50IiwidWFhIiwiaGVsbG9kamFuZ28tdnNiZmVpMDEiLCJoZWxsb2RqYW5nbyIsIm1kc3A6Y29yZTphZ20iXSwidGVuIjoidnNiZmVpMDEiLCJzY2hlbWFzIjpbInVybjpzaWVtZW5zOm1pbmRzcGhlcmU6aWFtOnYxIl0sImNhdCI6InVzZXItdG9rZW46djEifQ.UC-FvrZ3ZltqsL0_xyaaE-erR-9CtDUo6Y5c0ucMRQcnuJs85XvaX9yHxf3U4LToUW91eJpdp6SmeQA06i2aSuZaVlVUZRERsaiMPzthBgmJXsSTmRRmsbOFQ5bZzD8xmraDPqh693w9cEHHSdkzxGEoINOTst6AkM3lITYwnVpDGb_NJw1Rg-vqUDJwTpQondD3DCt_8U4hgjbgaiRXcwfbhGAqkyfHDjnTHoEW9FBKpXxBs4T-J5Bf97q3kVJQMEj3X0L1zEHSPdvSUM-eSSW-Jxouw-KoxVnrkc-DrphBAh57uKeddmxK011k1sXA7w6w1C4iy2XMAyLINr-x9A"

    request_com = GetFullTimeSerie(from_t, to_t, entity, serie_name, bearer_token)
    response = request_com.execute()
    data = request_com.execute()

    print("after response")
    with open("data.json", "w") as f:
        f.write(str(data))
    import json
#    data = json.dumps(str(response.json()))
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
    

#    x=np.linspace(-10,10,num=50).tolist()
#    y=[i**2 for i in x]
#    json_x=json.dumps([str(x)for x in x_date])

    return render(request, 'index.html', {'json_x':x_data, 'json_y':y_data, 'stuff' : bearer_token})
#    return render(request, 'index.html', {'stuff' :
#        str(request.META)})
