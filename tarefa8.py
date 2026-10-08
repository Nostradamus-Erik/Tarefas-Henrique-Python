lista = [
    {"Nome": "Celular", "Preco": 1500},
    {"Nome": "Estojo", "Preco": 50},
    {"Nome": "Quadro Negro", "Preco": 50},
]
for i in lista:
    if i["Preco"] >= 50.00:
        print(f"O produto {i["Nome"]} é maior que R$50.00 com seu valor de R$ {i["Preco"]}")