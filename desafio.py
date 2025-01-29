menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
LIMITE = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUE = 3
deposito = 0
saque = 0

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = float(input("Valor do depósito: "))
        if valor_deposito > 0:
            deposito += valor_deposito
            extrato += f"+ deposito de R$ {valor_deposito}\n"
            print("Valor depositado!")
        else:
            print('Valor negativo')
    elif opcao == 's':
        if numero_saque < LIMITE_SAQUE:
            valor_saque = float(input("Valor do saque: "))
            if valor_saque > LIMITE:
                print(f"Excedeu o limite de R$ {LIMITE}")
            elif valor_saque > saldo:
                print(f"Excedeu o saldo de R$ {saldo}")
            else:
                saque += valor_saque
                extrato += f"- saque de R$ {valor_saque}\n"
                numero_saque += 1
        else:
            print(f"Excedeu o número de Saque de {LIMITE_SAQUE}")
    elif opcao == 'e':
        saldo = deposito - saque
        print(f"==============Extrato==============")
        print(f'Saldo atual é de {saldo}')
        print(f'{extrato}')
    elif opcao == 'q':
        break
    else:
        print('opção inválida, selecione uma das operações desejadas')
