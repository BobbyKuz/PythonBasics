hour = int(input())
day_of_week = input()

if 10 <= hour < 18 and day_of_week == "Monday":
    print("open")
elif 10 <= hour < 18 and day_of_week == "Tuesday":
    print("open")
elif 10 <= hour < 18 and day_of_week == "Wednesday":
    print("open")
elif 10 <= hour < 18 and day_of_week == "Thursday":
    print("open")
elif 10 <= hour < 18 and day_of_week == "Friday":
    print("open")
elif 10 <= hour < 18 and day_of_week == "Saturday":
    print("open")
else:
    print("closed")

