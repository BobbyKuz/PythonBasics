budjet = float(input())
season = input().capitalize()

destination = ""
place = ""
expences = 0

if budjet <= 100:
    destination = "Bulgaria"
    if season == "Summer": 
        place = "Camp"
        expences = budjet * 0.30
    elif season == "Winter":
        place = "Hotel"
        expences = budjet * 0.70

elif budjet <= 1000:
    destination = "Balkans"
    if season == "Summer":
        place = "Camp"
        expences = budjet * 0.40
    elif season == "Winter":
        place = "Hotel"
        expences = budjet * 0.80

elif budjet >= 1000:
        destination = "Europe"
        place = "Hotel"
        expences = budjet * 0.90

print(f"Somewhere in {destination}")
print(f"{place} - {expences:.2f}")
        