import re, textwrap

def menu() -> int:
    menu = """
    Olá. O que deseja fazer?

    [0] Depositar
    [1] Sacar
    [2] Extrato
    [3] Criar novo usuário
    [4] Criar nova conta
    [5] Listar contas
    [6] Sair

    """

    return int(input(textwrap.dedent(menu)))


def exibir_extrato(saldo: float, /, *, extrato: str):

    print('----------------------------------Extrato----------------------------------')

    print("Não ocorreu nenhuma movimentação em sua conta.\n" if not extrato else extrato)
    
    print(f'Saldo: R$ {saldo:.2f}')
    print('---------------------------------------------------------------------------')


def existe_usuario(lista_clientes: list, cpf: int) -> bool:

    for cliente in lista_clientes:
        if cliente['cpf'] == cpf:
            return True
    
    return False


def listar_contas(lista_contas: list):
    
    print('----------------------------------Contas-----------------------------------')
    
    for conta in lista_contas:
        print(f'Nome do titular: {conta['usuario']['nome']}')
        print(f'Agência: {conta['agencia']}')
        print(f'Número da conta: {conta['numero_conta']}')
        print('---------------------------------------------------------------------------')


def sacar(*, saldo: float, valor: float, extrato: str, limite: float, numero_saques: int, limite_saques: int) -> tuple:
    
    if numero_saques < limite_saques and valor < limite and saldo > valor and valor > 0:
        saldo += valor
        numero_saques += 1
        extrato += f'Saque: R$ {valor:.2f}\n'

    elif numero_saques >= limite_saques:
        print("Não foi possível continuar com a operação. O número de saques diários foi ultrapassado!")

    elif valor >= limite:
        print("Não foi possível continuar com a operação. Valor informado é superior ao limite!")

    elif saldo <= valor:
        print("Não foi possível continuar com a operação. Valor a ser sacado é maior que o saldo!")

    else:
        print("Não foi possível continuar com a operação. Valor informado para saque é inferior ou igual a zero!")

    return saldo, extrato


def depositar(saldo: float, valor: float, extrato: str, /) -> tuple:
    
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
    
    else:
        print("Não foi possível continuar com a operação. Valor informado está incorreto para depósito!")

    return saldo, extrato


def criar_usuario(lista_clientes: list):

    nome = input('Nome: ')
    data_nascimento = input('Data de nascimento (Formato: dia/mês/ano): ')
    cpf = input('CPF (Formato: xxx.xxx.xxx-xx): ')
    cpf = re.sub(r'\D', '', cpf)

    if existe_usuario(lista_clientes, cpf):
        print("Não foi possível continuar com a operação. Usuário já existe!")
        return
    
    logradouro_numero = input('Logradouro e número (Formato: logradouro, nro): ')
    bairro = input('Bairro: ')
    cidade_estado = input('Cidade e estado (Formato: cidade/sigla do estado): ')

    endereco = logradouro_numero + ' - ' + bairro + ' + ' + cidade_estado

    cliente_novo = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    lista_clientes.append(cliente_novo)


def criar_conta(agencia: str, numero_conta: int, lista_clientes: list) -> list:
    
    cpf = input('CPF (Formato: xxx.xxx.xxx-xx): ')
    cpf = re.sub(r'\D', '', cpf)

    if existe_usuario(lista_clientes, cpf):

        for cliente in lista_clientes:
            if cliente['cpf'] == cpf:
                usuario = cliente

        conta_nova = {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }

        return conta_nova
    
    print("Não foi possível continuar com a operação. Usuário não existe!")


def main():
    LIMITE_SAQUES_DIARIOS = 3
    AGENCIA = "0001"

    limite = 500
    numero_saques = 0
    saldo = 0
    extrato = ""
    lista_clientes = []
    lista_contas = []

    opcao = menu()

    while (True):

        if opcao == 0:
            valor = float(input('Valor a ser depositado: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 1:
            valor = float(input('Valor a ser sacado: '))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES_DIARIOS)

        elif opcao == 2:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 3:
            criar_usuario(lista_clientes)

        elif opcao == 4:
            numero_conta = len(lista_contas)+1
            conta_nova = criar_conta(AGENCIA, numero_conta, lista_clientes)
            
            if conta_nova:
                lista_contas.append(conta_nova)

        elif opcao == 5:

            if len(lista_contas) != 0:
                listar_contas(lista_contas)

            else:
                print("Não foi possível continuar com a operação. Não há contas registradas!")

        elif opcao == 6:
            print("Agradecemos a sua preferência.\nVolte sempre ;)")
            break

        else:
            print("Opção inválida!!!")
        
        opcao = menu()

main()