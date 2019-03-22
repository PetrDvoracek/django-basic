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
        bearer_token="Bearer"

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

    return render(request, 'index.html', {'json_x':x_data, 'json_y':y_data, 'stuff' : bearer_token})

