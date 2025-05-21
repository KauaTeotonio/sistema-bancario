# Sistema Bancário em Python

def depositar(saldo, extrato):

    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES):

    valor = float(input("Informe o valor do saque: "))
    
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")

    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    menu = """
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
    => """
    
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)
        elif opcao == "e":
            mostrar_extrato(saldo, extrato)
        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema bancário!")
            break
        else:
            print("Operação inválida, por favor selecione novamente.")

# Executando o programa
if __name__ == "__main__":
    main()
