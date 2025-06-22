codigo_peca1, numero_peca1, valorUnitario1 = map(float, input().split(' '))
codigo_peca2, numero_peca2, valorUnitario2 = map(float, input().split(' '))

total = (numero_peca1 * valorUnitario1) + (numero_peca2 * valorUnitario2)
print(f"VALOR A PAGAR: R$ {total:.2f}")