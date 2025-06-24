##n1, n2, n3, n4 = map(float, input().split())
n1 = 2.0
n2 = 4
n3 = 7.5
n4 = 8

media = ((n1 * 2)+(n2 * 3)+(n3 * 4)+(n4 * 1)) / (2 + 3 + 4 + 1)
print(f"Media: {media:.1f}")
if(media >= 7.0):
    print("Aluno aprovado.")

elif(media < 5.0):
    print("Aluno reprovado.")  

else:
    print("Aluno em exame.")
    exameNota = float(input())
    print(f"Nota do exame: {exameNota:.1f}")
    
    media_final = (exameNota + media)/2
    if(media_final >= 5.0):
        print("Aluno aprovado.")
    else: 
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")


