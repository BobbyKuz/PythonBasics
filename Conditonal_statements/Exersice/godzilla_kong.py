budget = float(input())
people_num = int(input())
clothes = float(input())

decor = budget * 0.1

if people_num > 150:
    clothes -= clothes * 0.1

total_cost = decor + people_num * clothes

if total_cost <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_cost:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total_cost - budget:.2f} leva more.")

