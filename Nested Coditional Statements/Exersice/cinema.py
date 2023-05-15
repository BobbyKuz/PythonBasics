screening_type = input()
rows = int(input())
colums = int(input())

income = 0
capacity = rows * colums

if screening_type == "Premiere":
    income = capacity * 12.00

elif screening_type == "Normal":
    income = capacity * 7.5

elif screening_type == "Discount":
    income = capacity * 5.00

print(f"{income:.2f} leva")
