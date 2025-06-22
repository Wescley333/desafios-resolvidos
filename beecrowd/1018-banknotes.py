preco = int(input())

troco = 0

print(preco)

print(f"{preco//100:.0f} nota(s) de R$ 100,00")
troco = preco % 100

print(f"{troco//50:.0f} nota(s) de R$ 50,00")
troco = troco % 50

print(f"{troco//20:.0f} nota(s) de R$ 20,00")
troco = troco % 20

print(f"{troco//10:.0f} nota(s) de R$ 10,00")
troco = troco % 10

print(f"{troco//5:.0f} nota(s) de R$ 5,00")
troco = troco % 5

print(f"{troco//2:.0f} nota(s) de R$ 2,00")
troco = troco % 2

print(f"{troco//1:.0f} nota(s) de R$ 1,00")
troco = troco % 1