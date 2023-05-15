dogs_packs = int(input())
cats_packs = int(input())

dogs_price_pack = 2.50
cats_price_pack = 4

dogs_total = dogs_price_pack * dogs_packs
cats_total = cats_packs * cats_price_pack
total = dogs_total + cats_total

print(f"{total} lv.")

