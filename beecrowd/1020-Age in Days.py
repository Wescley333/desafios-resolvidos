x = int(input())

anos = x//365
meses = (x%365) // 30
dias = ((x%365) % 30)
print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")