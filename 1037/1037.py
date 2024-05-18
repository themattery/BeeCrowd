#Intervalo
valor = float(input("Valor: "))

um = [0,25]
dois = [25,50]
tres = [50,75]
quatro = [75,100]

if valor > 0 and valor <= 25:
    print(f"Intervalo {um}")
if valor > 25 and valor <= 50:
    print(f"Intervalo {dois}")
if valor > 50 and valor <= 75:    
    print(f"Intervalo {tres}")
if valor > 75 and valor <= 100:
    print(f"Intervalo {quatro}")
if valor > 100 and valor < 0:
    print("Fora de intervalo")