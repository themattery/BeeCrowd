numbers = [int(x) for x in input().split(' ')]
final_list = []


while numbers:
    menor = numbers[0]
    for i in range(1, len(numbers)):
        if menor > numbers[i]:
            menor = numbers[i]
    final_list.append(menor)
    numbers.remove(menor)
    
for i in final_list:
    print(i)