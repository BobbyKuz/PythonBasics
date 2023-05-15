pens_packs = int(input())
markers_packs = int(input())
detergent_packs = int(input())
discount = int(input()) / 100

pens = pens_packs * 5.80
markers = markers_packs * 7.20
detergent = detergent_packs * 1.20
all_materials = pens + markers + detergent
after_discount = all_materials - (all_materials * discount)

print(f"{after_discount}")