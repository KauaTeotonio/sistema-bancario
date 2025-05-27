# Sistema Bancário V2

usuarios = []
contas = []

def criar_usuario():
    cpf = input("Informe o CPF (apenas números): ").replace(".", "").replace("-", "")

    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("Erro! CPF já cadastrado.")
        return

    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")

    usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def criar_conta_corrente():
    cpf = input("Informe o CPF do titular da conta: ")
    usuario = next((user for user in usuarios if user["cpf"] == cpf), None)

    if not usuario:
        print("Erro! Usuário não encontrado. Cadastre o usuário primeiro.")
        return

    numero_conta = len(contas) + 1  # Gera número sequencial
    agencia = "0001"  # Agência fixa

    conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    contas.append(conta)
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")

def listar_contas():
    print("\n======== LISTA DE CONTAS BANCÁRIAS ========")
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']} ({conta['usuario']['cpf']})")
    print("==========================================")

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print("Operação falhou! O valor excede o limite permitido.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! Valor inválido.")

    return saldo, extrato, numero_saques

def extrato(saldo, *, extrato):
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
    
    [u] Criar usuário
    [c] Criar conta corrente
    [l] Listar contas
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
    => """

    saldo = 0
    limite = 500
    extrato_lista = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)

        if opcao == "u":
            criar_usuario()
        elif opcao == "c":
            criar_conta_corrente()
        elif opcao == "l":
            listar_contas()
        elif opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato_lista = depositar(saldo, valor, extrato_lista)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato_lista, numero_saques = saque(
                saldo=saldo, valor=valor, extrato=extrato_lista, limite=limite, 
                numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
            )
        elif opcao == "e":
            extrato(saldo, extrato=extrato_lista)
        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema bancário!")
            break
        else:
            print("Operação inválida, por favor selecione novamente.")

if __name__ == "__main__":
    main()