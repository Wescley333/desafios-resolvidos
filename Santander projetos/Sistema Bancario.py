menu = """

===========MENU=======================
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
======================================
digite a opcao desejada: 
"""

saldo = 2000
limite = 500 
extrato = ""
limite_saque = 0

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valordeposito = float(input("Digite o valor que deseja depositar: "))
        
        if valordeposito <= 0:
            print("Error! digite um numero positivo")
        else:
            saldo += valordeposito
            extrato += f"deposito de {valordeposito}\n"
            print("Valor depositado com sucesso")
    
    elif opcao == 2:
        valorsaque = float(input("Digite o valor a ser sacado: "))

        if valorsaque <= 0 or valorsaque > 500:
            print("valor incorreto!")
        if limite_saque == 3:
            print("Operação falhou, limete de saques diarios batidos")
        else:
            saldo =- valorsaque
            extrato += f"saque no valor de {valorsaque}\n"
            print("Valor sacado com sucesso")
            limite_saque += 1

    elif opcao == 3: 
        print("\n==========EXTRATO==============")
        print(extrato)
        print(f"Saldo: R${saldo:.2f}")
        print("=================================")


    elif opcao == 4:
        print("\naté a proxima\n")
        break

    else:
        print("Opcao incorreta! Tente novamente")

