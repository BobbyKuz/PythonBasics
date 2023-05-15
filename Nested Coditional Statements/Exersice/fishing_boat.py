budjet = int(input())
season = input() # "Spring", "Summer", "Autumn","Winter"
people_count = int(input())
price_boat = 0

if season == "Spring":
    price_boat = 3000
elif season == "Summer" or season == "Autumn":
    price_boat = 4200
elif season == "Winter":
    price_boat = 2600

if people_count <= 6:
    price_boat -= price_boat * 0.10
elif 7 <= people_count <= 11:
    price_boat -= price_boat * 0.15
elif people_count > 12:
    price_boat -= price_boat * 0.25

if people_count % 2 == 0 and season != "Autumn":
    price_boat = price_boat * 0.95

if budjet >= price_boat:
    print(f"Yes! You have {budjet - price_boat:.2f} leva left.")
else:
    print(f"Not enough money! You need {price_boat - budjet:.2f} leva.")




