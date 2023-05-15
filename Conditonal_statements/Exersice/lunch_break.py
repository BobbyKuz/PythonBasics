# Input
from  math import  ceil
movie_name = input()
movie_direction = int(input())
break_time = int(input())

# Logic
lunch_break = break_time / 8
relax_break = break_time / 4
free_time = break_time -(lunch_break + relax_break)

# Output
if free_time >= movie_direction:
    print(f"You have enough time to watch {movie_name} and left with {ceil(free_time - movie_direction)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(movie_direction - free_time)} more minutes.")