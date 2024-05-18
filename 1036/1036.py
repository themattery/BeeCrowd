import math
n = input(": ")
valores = []

for x in n.split():
    valores.append(float(x))

a, b, c = valores

delta = (b**2) - (4*a*c)

if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    r1 = ((-b + math.sqrt(delta)) / (2*a))
    r2 = ((-b - math.sqrt(delta)) / (2*a))
    print(f"R1 = {round(r1, 5)}\nR2 = {round(r2, 5)}")
