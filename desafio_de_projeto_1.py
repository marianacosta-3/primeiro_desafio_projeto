menu = '''

================== Seja Bem-vindo! ==================

Digite o código para a operação que deseja realizar:

[s] Saque
[d] Depósito
[e] Extrato
[q] Sair


=>'''

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito R${valor:.2f}\n"
            print(f"Depósito realizado com sucesso! Seu saldo atual é R$ {saldo:.2f}")

        else:
            print("Operação falhou, formato informado inválido!")

    elif opcao == "s":
    
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_de_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente. Operação não realizada!")

        elif excedeu_limite:
            print("Limite excedido. Operação não realizada!")

        elif excedeu_saques:
            print("Número diário de saques excedido. Operação não realizada!")

        elif valor > 0:
            saldo -=valor
            numero_de_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"Saque realizado com sucesso! Seu saldo atual é R$ {saldo:.2f}")

        else:
            print("Operação falhou! O valor informado é inválido.")
       

    elif opcao == "e":
        print("================= EXTRATO =================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
        print("===========================================")


    elif opcao == "q":
        break

    else:
        print("Opção inválida! Tente novamente.")
