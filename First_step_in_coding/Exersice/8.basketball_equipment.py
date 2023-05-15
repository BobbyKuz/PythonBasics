year_fee = int(input())

shoes_price = year_fee - (year_fee * (40 / 100))
gear_price = shoes_price - (shoes_price * (20 / 100))
ball_price = gear_price / 4
acessories = ball_price / 5
equipment = year_fee + shoes_price + gear_price + ball_price + acessories

print(equipment)