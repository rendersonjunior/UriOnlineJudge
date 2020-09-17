#Time Conversion
def transform_time(time,type_time):
    return int((time - (time % type_time)) / type_time)

def rest_time(time,qtd_time):
    return int(time-qtd_time)

time_event = int(input())

# 1 hour: 3600 seconds
# 1 minute: 60 seconds

hours =  transform_time(time_event,3600)
time_event = rest_time(time_event,3600*hours)
minutes = transform_time(time_event,60)
time_event = rest_time(time_event,60*minutes)
seconds = int(time_event)

print(str(hours)+":"+str(minutes)+":"+str(seconds))