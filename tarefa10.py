boletim = {}
desejaadicionaraluno = input("Deseja adicionar alunos? S/N?")

while desejaadicionaraluno == "N" or "n":
    break

while desejaadicionaraluno == "S" or "s":
    
    Nome = input("Qual o nome do aluno que deseja adicionar? ")
    Nota = float(input("Qual a nota do aluno? "))
    
    boletim ["Nome"] = Nome
    boletim ["Nota"] = Nota
    
    for aluno in boletim:
     if aluno == "Nota":
      if boletim[aluno] >= 6.0:
        print("Aprovado")
   
      else:
        print("Reprovado")  
    
        
    sair = input("Deseja sair? S/N: ")
    if sair == "S" or "s":
      break 
        