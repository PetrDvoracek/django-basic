from django.shortcuts import render
import json
import numpy as np
import dateutil.parser
import datetime


def index(request):
    import requests
    
    url = "https://gateway.eu1.mindsphere.io/api/iottimeseries/v3/timeseries/7f03ff1dc93941e69c09dfc63389d43e/One"
    
    querystring = {"from":"2019-01-31T12:44:46.196Z"}
#    bearer_token = str(request.META['HTTP_AUTHORIZATION'])
    bearer_token="Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImtleS1pZC0xIiwidHlwIjoiSldUIn0.eyJqdGkiOiIxMjEyZWRkZDk0ZDM0ODRhOGE5MzM1MWNkZTg5ZTdjMSIsInN1YiI6IjYzNDdkMmFhLTRlMGQtNGY0MS04MDcxLTcwZTQ4ZWQwNTk4OSIsInNjb3BlIjpbImhlbGxvZGphbmdvLnNjb3BlIiwibWRzcDpjb3JlOmFnbS5mdWxsYWNjZXNzIiwibWRzcDpjb3JlOmFzc2V0bWFuYWdlbWVudC5hZG1pbiIsIm1kc3A6Y29yZTppb3QuZmlsQWRtaW4iLCJtZHNwOmNvcmU6aW90LmJ1bGtUaW1Vc2VyIiwibWRzcDpjb3JlOmlvdC5idWxrVGltQWRtaW4iLCJ1YWEub2ZmbGluZV90b2tlbiIsIm1kc3A6Y29yZTppb3QudGltQWRtaW4iLCJtZHNwOmNvcmU6aW90LnRpbVVzZXIiLCJtZHNwOmNvcmU6aW90LmZpbFVzZXIiXSwiY2xpZW50X2lkIjoiaGVsbG9kamFuZ28tdnNiZmVpMDEiLCJjaWQiOiJoZWxsb2RqYW5nby12c2JmZWkwMSIsImF6cCI6ImhlbGxvZGphbmdvLXZzYmZlaTAxIiwiZ3JhbnRfdHlwZSI6ImF1dGhvcml6YXRpb25fY29kZSIsInVzZXJfaWQiOiI2MzQ3ZDJhYS00ZTBkLTRmNDEtODA3MS03MGU0OGVkMDU5ODkiLCJvcmlnaW4iOiJ2c2JmZWkwMSIsInVzZXJfbmFtZSI6InBldHIuZHZvcmFjZWtAdnNiLmN6IiwiZW1haWwiOiJwZXRyLmR2b3JhY2VrQHZzYi5jeiIsImF1dGhfdGltZSI6MTU1Mjg5ODQ2NywicmV2X3NpZyI6Ijc5N2NlYWUyIiwiaWF0IjoxNTUyODk4NDY4LCJleHAiOjE1NTI5MDAyNjgsImlzcyI6Imh0dHBzOi8vdnNiZmVpMDEucGlhbS5ldTEubWluZHNwaGVyZS5pby9vYXV0aC90b2tlbiIsInppZCI6InZzYmZlaTAxIiwiYXVkIjpbIm1kc3A6Y29yZTppb3QiLCJtZHNwOmNvcmU6YXNzZXRtYW5hZ2VtZW50IiwidWFhIiwiaGVsbG9kamFuZ28tdnNiZmVpMDEiLCJoZWxsb2RqYW5nbyIsIm1kc3A6Y29yZTphZ20iXSwidGVuIjoidnNiZmVpMDEiLCJzY2hlbWFzIjpbInVybjpzaWVtZW5zOm1pbmRzcGhlcmU6aWFtOnYxIl0sImNhdCI6InVzZXItdG9rZW46djEifQ.ZeNKNFhPd-cZVYFxdsHFc0R8xxrisXtf-hQr1Lmns1RiIaXxMjJqm2J6uxpZTtw5Cid23sfnbruqCkvj1B4mVDGm5QRA1cRIC1u8NNf5ShUr0c-8yyLuTtJBZvdq4k34cIv5vSQwEbIy5BHC4ueCO98oMoR8bWhBtVvHpWE8OdTsLhe-XQR4cqolHB-fAtKW-8JjcophH-aNJSGlQz-pgdUeYt6j0HB2u4PmKZovb3ZTHUEMh5kSjLKip-HoGi6RRszSpPMzPTIu5Y5VInuCwsGW1paIYAyZ5pwTAHTjK3dIaM4dCCgOnSifwQ43Vf19ICevTiWwyxSvgY_s-Bejrg"
    payload = ""
    headers = {
        'Authorization': bearer_token,
        'cache-control': "no-cache",
        'Postman-Token': "325f46de-27d9-4a0b-a1f5-4bde202ab999"
        }
    
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    with open("data.json", "w") as f:
        f.write(str(response.json()))
    import json
#    data = json.dumps(str(response.json()))
    data = response.json()
    print(data[0]['_time'])
    x_date_string=["2019-01-31T13:52:45.223Z","2019-01-31T13:52:50.223Z"]
    x_date = [dateutil.parser.parse(x)for x in x_date_string]
    y_date = [1,2]
    x_data=[]
    y_data=[]
    for x in data:
        if 'One' in x.keys():
            x_data.append(x['_time'])
            y_data.append(x['One'])
        else:
            print(x)
    

#    x=np.linspace(-10,10,num=50).tolist()
#    y=[i**2 for i in x]
#    json_x=json.dumps([str(x)for x in x_date])
    json_x=json.dumps(x_date_string)
    json_y=json.dumps(y_date)
    return render(request, 'index.html', {'json_x':x_data, 'json_y':y_data, 'stuff' : bearer_token})
#    return render(request, 'index.html', {'stuff' :
#        str(request.META)})
