temp = int(input())
time_of_day = input()

Outfit = ""
Shoes = ""

if 10 <= temp <= 18:
    if time_of_day == "Morning":
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif time_of_day == "Afternoon":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif time_of_day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"

elif 18 < temp <= 24:
    if time_of_day == "Morning":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif time_of_day == "Afternoon":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif time_of_day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"

        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif time_of_day == "Afternoon":
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
    elif time_of_day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"

print(f"It's {temp} degrees, get your {Outfit} and {Shoes}.")


