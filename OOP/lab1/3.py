time = [int(q) for q in input().split(' ')]
hour, minute = [(e - q) for q, e in zip(time, time[2:])]

if minute > 15 or hour:
    remain = bool(minute)
    if hour + remain > 6: 
        print(200)
    else: 
        if hour + remain > 3:
            hour = 3*(hour-2) + remain
        print((hour + remain) * 10)
else:
    print(0)