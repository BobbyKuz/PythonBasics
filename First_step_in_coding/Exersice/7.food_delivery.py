# for one menu - chicken 10.35 fish 12.40 Vegan 8.15
chicken_menus = int(input())
fish_menus = int(input())
vegan_menus = int(input())

chicken_price = chicken_menus * 10.35
fish_price = fish_menus * 12.40
vegan_price = vegan_menus * 8.15
total_price = chicken_price + fish_price + vegan_price
desert_price = total_price * (20 / 100)
delivery = 2.5
all_price = total_price + desert_price + delivery

print(f"{all_price:.2f}")
