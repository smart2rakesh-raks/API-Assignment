from django.http import JsonResponse
from django.shortcuts import render
import json
import datetime
from .questions.question1 import production_count
from .questions.question2 import (runtime_downtime, d_time, utlite)

# Create your views here.
def index(request):
    return render(request, 'index.html')

def question1(request):
    with open("/pro1/web/api/JsonData/json_1.json",'r') as f:
        data=json.load(f)

    start_time = "2021-01-28T07:30:00Z"
    end_time = "2021-01-28T13:30:00Z"

    result = {
        "shiftA": {"production_A_count": 0, "production_B_count": 0},
        "shiftB": {"production_A_count": 0, "production_B_count": 0},
        "shiftC": {"production_A_count": 0, "production_B_count": 0},
    }
    if start_time and end_time:
        result = production_count(start_time, end_time, data,result)

    return JsonResponse(result)


def question2(request):
    runtime = datetime.timedelta(0)
    downtime = datetime.timedelta(0)
    utilisation = 0
    with open("/pro1/web/api/JsonData/json_2.json", 'r') as f:
        data = json.load(f)

    start_time = "2021-01-28T08:30:00Z"
    end_time = "2021-01-28T10:30:00Z"

    if start_time and end_time:
        runtime, downtime = runtime_downtime(start_time,end_time,data)
    utilisation = utlite(runtime, downtime)
    return JsonResponse({
        "runtime": d_time(runtime),
        "downtime": d_time(downtime),
        "utilisation": round(utilisation, 2)
    })




