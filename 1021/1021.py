n = float(input())
resto = n

# 100
cem = resto//100
resto = resto%100
# 50
cinq = resto//50
resto = resto%50
# 20
vinte = resto//20
resto = resto%20
# 10
dez = resto//10
resto = resto%10
# 5
cinco = resto//5
resto = resto%5
# 2
dois = resto//2
resto = resto%2

#1
um = resto//1
resto = resto%1
#0.50
cinq_cent = resto//0.50
resto = resto%0.50
#0.25
vinte_cent = resto//0.25
resto = resto%0.25
#0.10
dez_cent = resto//0.10
resto = resto%0.10
#0.05
cinco_cent = resto//0.05
resto = resto%0.05
#0.01
um_cent = resto//0.01


print(f"NOTAS:")
print(f"{int(cem)} nota(s) de R$ 100.00")
print(f"{int(cinq)} nota(s) de R$ 50.00")
print(f"{int(vinte)} nota(s) de R$ 20.00")
print(f"{int(dez)} nota(s) de R$ 10.00")
print(f"{int(cinco)} nota(s) de R$ 5.00")
print(f"{int(dois)} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{int(um)} moeda(s) de R$ 1.00")
print(f"{int(cinq_cent)} moeda(s) de R$ 0.50")
print(f"{int(vinte_cent)} moeda(s) de R$ 0.25")
print(f"{int(dez_cent)} moeda(s) de R$ 0.10")
print(f"{int(cinco_cent)} moeda(s) de R$ 0.05")
print(f"{int(um_cent)} moeda(s) de R$ 0.01")