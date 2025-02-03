# Trilha do projeto Sistema Bancário com Python. As atividade são: depositar, sacar e extrato.
def sacar(*, saldo, valor_saque, limite, limite_saque):
    global saque, extrato, numero_saque
    if numero_saque < limite_saque:
        if valor_saque > limite:
            print(f"Excedeu o limite de R$ {limite}")
        elif valor_saque > saldo:
            print(f"Excedeu o saldo de R$ {saldo}")
        else:
            saque += valor_saque
            extrato += f"- saque de R$ {valor_saque}\n"
            numero_saque += 1
            return saldo, extrato
    else:
        print(f"Excedeu o número de Saque de {limite_saque}")

def depositar(valor_deposito, /):
    global deposito, extrato
    if valor_deposito > 0:
        deposito += valor_deposito
        extrato += f"+ deposito de R$ {valor_deposito}\n"
        print("Valor depositado!")
    else:
        print('Valor negativo')
    return valor_deposito, extrato

def extrair(saldo, extrato = None):
    print(f"==============Extrato==============")
    print(f'Saldo atual é de {saldo}')
    print(f'{extrato}')

def lista_usuarios(cpf):
    global usuarios
    flag = True
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            flag = False
    return flag

def criar_usuario(nome, data_nascimento, cpf, endereco):
    global usuarios
    if lista_usuarios(cpf):
        usuarios.append({
            'nome': nome,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'endereco': endereco
        })
    else:
        print('usuário já existe, tente outro cpf')
    return usuarios

def criar_conta(agencia, conta, cpf):
    global contas
    if not lista_usuarios(cpf):
        contas.append({
            'agencia': agencia,
            'conta': conta,
            'cpf': cpf
        })
    else:
        print('usuário não existe, cadastre o cpf')
    return contas


menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta
[q] Sair
"""
usuarios = []
contas = []
saldo = 0
LIMITE = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUE = 3
deposito = 0
saque = 0

while True:
    opcao = input(menu + "> ")

    if opcao == 'd':
        valor_deposito = float(input("Valor do depósito: "))
        resultado = depositar(valor_deposito)
        print(resultado)

    elif opcao == 's':
        valor_saque = float(input("Valor do saque: "))
        resultado = sacar(saldo=saldo, 
            valor_saque=valor_saque,
            limite=LIMITE,
            limite_saque=LIMITE_SAQUE)
        print(resultado)
    elif opcao == 'e':
        saldo = deposito - saque
        extrair(saldo, extrato=extrato)
    elif opcao == 'u':
        nome = input('nome: ')
        data_nascimento = input('Data nascimento, dd/mm/aaaa: ')
        cpf = input('cpf: ')
        endereco = input('rua, numero - bairro - cidade/estado: ')
        resultado = criar_usuario(nome, data_nascimento, cpf, endereco)
        print(resultado)
    elif opcao == 'c':
        agencia = input('Entre com a agênia: ')
        conta = input('Entre com a conta: ')
        cpf = input('Entre com o cpf: ')
        resultado = criar_conta(agencia, conta, cpf)
        print(resultado)
    elif opcao == 'q':
        break
    else:
        print('opção inválida, selecione uma das operações desejadas')
