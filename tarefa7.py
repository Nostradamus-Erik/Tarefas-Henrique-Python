senha = 10101856
digitacaosenha = int(input("Digite sua senha: "))

while digitacaosenha != senha:
    digitacaosenha = int(input("Senha incorreta, digite novamente: "))

    if digitacaosenha == senha:
        print("Acesso liberado")
        break
    break