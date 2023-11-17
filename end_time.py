hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

total_minutes = mins + dura

extra_hours = total_minutes // 60

new_mins = total_minutes % 60

total_hours = hour + extra_hours

if (total_hours > 23):
    while (total_hours > 23):
        total_hours -= 24

print(str(total_hours) + ":" + str(new_mins))
