#  Sistema Bancário V3 - Com POO

from datetime import date

class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class ContaBancaria:
    def __init__(self, cliente, numero_conta, agencia="0001"):
        self.cliente = cliente
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.saldo = 0
        self.extrato = []
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Erro! Valor inválido.")

    def sacar(self, valor, limite, limite_saques, numero_saques):
        if valor > self.saldo:
            print("Erro! Saldo insuficiente.")
        elif valor > limite:
            print("Erro! Valor excede o limite permitido.")
        elif numero_saques >= limite_saques:
            print("Erro! Número máximo de saques atingido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Erro! Valor inválido.")
        
    def mostrar_extrato(self):
        print("\n===== EXTRATO =====")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")

def criar_cliente():
    nome = input("Informe o nome: ")
    cpf = input("Informe o CPF (apenas números): ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")

    cliente = Cliente(nome, cpf, data_nascimento, endereco)
    print("Usuário cadastrado com sucesso!")
    return cliente

def criar_conta(cliente, numero_conta):
    conta = ContaBancaria(cliente, numero_conta)
    cliente.adicionar_conta(conta)
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
    return conta

def listar_contas(clientes):
    print("\n======== LISTA DE CONTAS BANCÁRIAS ========")
    if not clientes:
        print("Nenhuma conta cadastrada.")
    else:
        for cliente in clientes:
            for conta in cliente.contas:
                print(f"Agência: {conta.agencia} | Conta: {conta.numero_conta} | Titular: {cliente.nome} ({cliente.cpf})")
    print("==========================================")

def main():
    clientes = []
    numero_conta = 1
    LIMITE_SAQUES = 3
    limite = 500

    menu = """
    
    [u] Criar usuário
    [c] Criar conta corrente
    [l] Listar contas
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
    => """

    while True:
        opcao = input(menu)

        if opcao == "u":
            cliente = criar_cliente()
            clientes.append(cliente)
        elif opcao == "c":
            cpf = input("Informe o CPF do titular da conta: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente:
                conta = criar_conta(cliente, numero_conta)
                numero_conta += 1
            else:
                print("Erro! Usuário não encontrado.")
        elif opcao == "l":
            listar_contas(clientes)
        elif opcao == "d":
            cpf = input("Informe o CPF do titular: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente and cliente.contas:
                valor = float(input("Informe o valor do depósito: "))
                cliente.contas[0].depositar(valor)
            else:
                print("Erro! Conta não encontrada.")
        elif opcao == "s":
            cpf = input("Informe o CPF do titular: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente and cliente.contas:
                valor = float(input("Informe o valor do saque: "))
                cliente.contas[0].sacar(valor, limite, LIMITE_SAQUES, 0)  # Controle de saques pode ser melhorado
            else:
                print("Erro! Conta não encontrada.")
        elif opcao == "e":
            cpf = input("Informe o CPF do titular: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente and cliente.contas:
                cliente.contas[0].mostrar_extrato()
            else:
                print("Erro! Conta não encontrada.")
        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema bancário!")
            break
        else:
            print("Operação inválida, por favor selecione novamente.")

if __name__ == "__main__":
    main()