from math import pi
figure = input()
a = float(input())
area = 0

if figure == "square":
    area = a * a
    print(f"{area:.3f}")
elif figure == "rectangle":
    b = float(input())
    area = a * b
    print(f"{area:.3f}")
elif figure == "circle":
    area = pi * a * a
    print(f"{area:.3f}")
else:
    c = float(input())
    area = (a * c) / 2
    print(f"{area:.3f}")
