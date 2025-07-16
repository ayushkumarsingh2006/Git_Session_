#if u are running with 10km in 42min 42 sec,
#calculate the average pace in time per mile in minute and sec
#calculate the average speed in miles per hour






distance = int(input("enter the distance"))
dist_in_miles = distance*0.621

time_min = int(input("enter the time in min"))
time_sec = int(input("enter the time in sec"))

time_hour = time_min/60 + time_sec/(60*60)

total_time = time_min + time_sec/60

avg_pace = total_time/ dist_in_miles
pace_min = int(avg_pace)
pace_sec = int((avg_pace - pace_min)*60)

avg_speed = dist_in_miles/ time_hour


print("average pace is", pace_min,"min",pace_sec,"sec per hour")
print("average speed is", avg_speed ,"mph")
