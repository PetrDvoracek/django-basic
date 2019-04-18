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
        bearer_token="Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vdnNiZmVpMDEubG9jYWxob3N0OjgwODAvdWFhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktaWQtMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJjOTQzOWRjNmNmMmM0MjMzYTM0MDQwM2M2YzFjNjg0MiIsInN1YiI6IjYzNDdkMmFhLTRlMGQtNGY0MS04MDcxLTcwZTQ4ZWQwNTk4OSIsInNjb3BlIjpbImhlbGxvZGphbmdvLnNjb3BlIiwibWRzcDpjb3JlOmFnbS5mdWxsYWNjZXNzIiwibWRzcDpjb3JlOmFzc2V0bWFuYWdlbWVudC5hZG1pbiIsIm1kc3A6Y29yZTppb3QuZmlsQWRtaW4iLCJtZHNwOmNvcmU6aW90LmJ1bGtUaW1Vc2VyIiwibWRzcDpjb3JlOmlvdC5idWxrVGltQWRtaW4iLCJ1YWEub2ZmbGluZV90b2tlbiIsIm1kc3A6Y29yZTppb3QudGltQWRtaW4iLCJtZHNwOmNvcmU6aW90LnRpbVVzZXIiLCJtZHNwOmNvcmU6aW90LmZpbFVzZXIiXSwiY2xpZW50X2lkIjoiaGVsbG9kamFuZ28tdnNiZmVpMDEiLCJjaWQiOiJoZWxsb2RqYW5nby12c2JmZWkwMSIsImF6cCI6ImhlbGxvZGphbmdvLXZzYmZlaTAxIiwiZ3JhbnRfdHlwZSI6ImF1dGhvcml6YXRpb25fY29kZSIsInVzZXJfaWQiOiI2MzQ3ZDJhYS00ZTBkLTRmNDEtODA3MS03MGU0OGVkMDU5ODkiLCJvcmlnaW4iOiJ2c2JmZWkwMSIsInVzZXJfbmFtZSI6InBldHIuZHZvcmFjZWtAdnNiLmN6IiwiZW1haWwiOiJwZXRyLmR2b3JhY2VrQHZzYi5jeiIsImF1dGhfdGltZSI6MTU1NTU5ODc0OSwicmV2X3NpZyI6IjVlZTA4ZmJhIiwiaWF0IjoxNTU1NTk4NzQ5LCJleHAiOjE1NTU2MDA1NDksImlzcyI6Imh0dHBzOi8vdnNiZmVpMDEucGlhbS5ldTEubWluZHNwaGVyZS5pby9vYXV0aC90b2tlbiIsInppZCI6InZzYmZlaTAxIiwiYXVkIjpbIm1kc3A6Y29yZTppb3QiLCJtZHNwOmNvcmU6YXNzZXRtYW5hZ2VtZW50IiwidWFhIiwiaGVsbG9kamFuZ28tdnNiZmVpMDEiLCJoZWxsb2RqYW5nbyIsIm1kc3A6Y29yZTphZ20iXSwidGVuIjoidnNiZmVpMDEiLCJzY2hlbWFzIjpbInVybjpzaWVtZW5zOm1pbmRzcGhlcmU6aWFtOnYxIl0sImNhdCI6InVzZXItdG9rZW46djEifQ.Z_fW_6aXugeVSoVYaiekqQcadpTQeXfIdiBOEoQJVjwTU4Pr6eLvCxJUH_vITjMgkO6kIBKmoNC8hPLy9NzaTK2caBLSiMvQPHQuQ0cGSZopZwA86Hhvu1c6UJ6YOr5insMgZxM5rOawQnS9nIbMLPf5cO8UIhCy9CwattKtQDgKbMgoyxki6WnUAgBYFvx7yAyrVXFyW50QCoz0CE5mWkm9vLgP9UUclgHFUgi5HW0sSFbhur54CLEAmMLZt6NACYH3iC_m9MxuzfIZ0Y0nCAuDtZy1ythqBzHwOg5fzEsraWlILaNCHWW9zQjJJHZtRhQxH_kO6A3EoWX3JDjYoQ"

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

    return render(request, 'index_new.html', {'json_x':x_data, 'json_y':y_data, 'stuff' : bearer_token})

