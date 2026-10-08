palavra = input("Digite uma palavra: ")
vogais = []

for i in palavra:
    if i in "aeiouAEIOU":
      vogais.append (i)
print(vogais)