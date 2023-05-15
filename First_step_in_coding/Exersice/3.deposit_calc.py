deposit_amount = float(input())
time_deposit = int(input())
intrest = float(input())

all_intrest = deposit_amount * (intrest / 100)
monthly_intrest = all_intrest / 12
total = deposit_amount + time_deposit * monthly_intrest

print(total)
