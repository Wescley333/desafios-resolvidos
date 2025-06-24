cardapio = {
1 : 4.00,
2 : 4.50,
3 : 5.00,
4 : 2.00,
5 : 1.50
} 
item, quantidade = map(int, input().split())


if item in cardapio:
    total = cardapio[item] * quantidade
    print(f"Total: R${total:.2f}")

    