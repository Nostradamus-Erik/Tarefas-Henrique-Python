senha = 10101856
digitacaosenha = int(input("Digite sua senha: "))

while digitacaosenha != senha:
    print("Senha incorreta, digite novamente")
    digitacaosenha = int(input("Digite sua senha: "))

    if digitacaosenha == senha:
        print("Acesso liberado")
        break
