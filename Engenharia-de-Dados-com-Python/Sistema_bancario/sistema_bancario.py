menu = """
Olá. O que deseja fazer?

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

"""

LIMITE_SAQUES_DIARIOS = 3
limite = 500
numero_saques = 0
saldo = 0
extrato = ""

opcao = int(input(menu))

while opcao != 3:

    if opcao == 0:
        valor = float(input("Quanto deseja depositar? "))

        if valor <= 0:
            print("Não foi possível continuar com a operação. Valor informado incorreto para depósito!")
            continue
        
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'

    elif opcao == 1:
        if numero_saques >= LIMITE_SAQUES_DIARIOS:
            print("Não foi possível continuar com a operação. Limite de saques diários excedido!")
        
        else:
            valor = float(input("Quanto deseja sacar? "))

            if valor >= 500:
                print("Não foi possível continuar com a operação. Valor do saque acima do limite!")
                continue

            elif (saldo - valor) < 0:
                print("Não foi possível continuar com a operação. Não há saldo suficiente!")
                continue

            saldo -= valor
            numero_saques += 1
            extrato += f'Saque: R$ {valor:.2f}\n'

    elif opcao == 2:
        print('----------------------------------Extrato----------------------------------')

        print("Não ocorreu nenhuma movimentação em sua conta.\n" if not extrato else extrato)
        
        print(f'Saldo: R$ {saldo:.2f}')
        print('---------------------------------------------------------------------------')

    else:
        print("Opção inválida!!!")
        break

    opcao = int(input(menu))