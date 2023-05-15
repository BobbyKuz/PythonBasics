from unittest import result

exam_hour = int(input())
exam_minute = int(input())

student_hour = int(input())
student_minute = int(input())

exam_time_in_minutes = (exam_hour * 60) + exam_minute
student_time_in_minutes = (student_hour * 60) + student_minute

time_diff = exam_time_in_minutes - student_time_in_minutes

if time_diff > 30:
    print("Early")
elif time_diff < 0:
    print("Late")
else:
    print("On time")

hour = 0
minute = abs(time_diff)

result = ""

if minute >= 60:
    hour = minute // 60
    minute = minute % 60

if hour > 0:
    result += f"{hour}:{minute:02d} hours "
elif minute > 0:
    result += f"{minute} minutes "

if time_diff > 0:
    result += "before the start"
elif time_diff < 0:
    result += "after the start"

print(result)
