notas = [float(x) for x in input().strip().split(' ')] #must get further into list comp.

def avaliarMedia(media):
    if media>=7.0:
        print("Aluno aprovado.")
    elif media<5.0:
        print("Aluno reprovado.")
    else:
        avaliarExame(media)
    
def avaliarExame(media):
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame}")
    media = (media+nota_exame)/2
    if media>=5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")
    
media = ((notas[0]*2)+(notas[1]*3)+(notas[2]*4)+notas[3])/10

print(f"Media: {media:.1f}")
avaliarMedia(media)