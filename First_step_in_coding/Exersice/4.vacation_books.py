pages = int(input())
pages_per_hour = int(input())
num_days_necessary = int(input())

all_hours = pages / pages_per_hour
necessary_hours_day = all_hours / num_days_necessary

print(round(necessary_hours_day))