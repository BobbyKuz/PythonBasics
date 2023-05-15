lenght = int(input())
width = int(input())
high = int(input())
precent_taken = float(input())

volume_cubic_cm = lenght * width * high
litre = volume_cubic_cm / 1000
taken_volume = precent_taken / 100
necessery_litres = litre * (1 - taken_volume)

print(necessery_litres)
