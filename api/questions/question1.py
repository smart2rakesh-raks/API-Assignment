import datetime

SHIFT_A = datetime.time(0, 30, 0)
SHIFT_B = datetime.time(8, 30, 0)
SHIFT_C = datetime.time(14, 30, 0)

def production_count(start_time, end_time, data, result):

    start_time = datetime.datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ')
    end_time = datetime.datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%SZ')

    for obj in data:
        cur_time = datetime.datetime.strptime(obj["time"],'%Y-%m-%d %H:%M:%S')
        if start_time <= cur_time <= end_time:
            if SHIFT_A <= cur_time.time() <= SHIFT_B:
                shift = 'shiftA'
            elif SHIFT_B <= cur_time.time() <= SHIFT_C:
                shift = 'shiftB'
            else:
                shift = 'shiftC'
            if obj['production_A']:
                result[shift]['production_A_count'] += 1
            if obj['production_B']:
                result[shift]['production_B_count'] += 1
    return result