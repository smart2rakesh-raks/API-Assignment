import datetime

def runtime_downtime(start_time, end_time, data):

    start_time = datetime.datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ')
    end_time = datetime.datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%SZ')
    r = 0
    d = 0

    for obj in data:
        cur_time = datetime.datetime.strptime(obj["time"], '%Y-%m-%d %H:%M:%S')
        if start_time <= cur_time <= end_time:
            if obj['runtime'] > 1021:
                r += 1021
                d += obj['runtime'] - 1021
            else: 
                r += obj['runtime']
            d += obj['downtime']
    return datetime.timedelta(seconds=r), datetime.timedelta(seconds=d)


def d_time(time):
    seconds = time.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{hours}h:{minutes}m:{seconds}s'

def utlite(runtime, downtime):
    if runtime.seconds + downtime.seconds:
        return ( runtime.seconds/(runtime.seconds + downtime.seconds) ) * 100
    else:
        return 0