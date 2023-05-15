holiday_price = float(input())
puzzels = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

rent = 0
profit = 0

all_toys_cost = puzzels * 2.60 + dolls * 3 + bears * 4.10 + \
    minions * 8.20 + trucks * 2
all_toys = puzzels + dolls + bears + minions + trucks
discount = 0
final_cost = 0

if all_toys >= 50:
    discount += 0.25 * all_toys_cost

final_cost = all_toys_cost - discount
rent += 0.1 * final_cost
profit = final_cost - rent

if profit >= holiday_price:
    print(f"Yes! {profit - holiday_price:.2f} lv left.")
else:
    print(f"Not enough money! \
         {holiday_price - profit:.2f} lv needed.")
