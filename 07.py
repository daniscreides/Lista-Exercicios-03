#Escreva um programa que possa ler do usuário uma senha e verificar se a senha digitada é igual a "abc123". Neste programa, o usuário tem, no máximo, 3 tentativas de acertar a senha (insira entradas inválidas para verificar se o número de tentativas irá expirar com sucesso). A cada vez que o usuário errar a senha, exiba uma mensagem de erro e quantas tentativas ainda lhe restam.

tentativas= 3

for i in range (3):
  senha=input("Senha: ")
  if senha == "abc123":
    print ("Parabéns, senha correta.")
    break
  else:
    tentativas = tentativas - 1
    print("Restam " + str(tentativas) + " tentativas restantes.")
  if tentativas == 0:
    print ("Usuário bloqueado! ")