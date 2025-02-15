menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo, deposito):
    saldo += deposito
    return saldo

def sacar(numero_saques, saldo, saque):
    saldo -= saque
    numero_saques += 1
    return numero_saques, saldo

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo = depositar(saldo, valor)
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Você não tem saldo suficiente.")

        elif valor > limite:
            print("O valor do saque excede o limite.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques excedido.")

        elif valor > 0:
            numero_saques, saldo = sacar(numero_saques, saldo, valor)
            extrato += f"Saque: R$ {valor:.2f}\n"
            
        else:
            print("O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("NSem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

