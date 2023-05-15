from math import floor

record = float(input())
distance = float(input())
sec_per_meter = float(input())

needed_time = distance * sec_per_meter
slowdown = (floor(distance / 15)) * 12.5
total_time = needed_time + slowdown

if total_time > record:
    print(f"No, he failed! He was {total_time - record:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")