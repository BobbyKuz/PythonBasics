budget = float(input())
videocards = int(input())
cpu = int(input())
ram = int(input())

videocards_price = videocards * 250
cpu_price = videocards_price * 0.35 * cpu
ram_price = videocards_price * 0.10 * ram
total = videocards_price + cpu_price + ram_price

if videocards > cpu:
    total -= total * 0.15

if budget > total:
    print(f"You have {budget - total} leva left!")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva more!")

# if videocards > cpu:
