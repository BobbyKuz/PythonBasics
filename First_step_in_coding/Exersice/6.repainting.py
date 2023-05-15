nylon = int(input())
paint = int(input())
tinner = int(input())
hours_necessery = int(input())

amount_nylon = (nylon + 2) * 1.50
amount_paint = (paint + paint/10) * 14.50
amount_tinner = tinner * 5
bags = 0.40
total = amount_nylon + amount_paint + amount_tinner + bags
cost_labour = (total * (30 / 100)) * hours_necessery
final_cost = total + cost_labour

print(final_cost)