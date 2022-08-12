#Escreva um programa que possa ler o nome de um aluno e um conjunto de notas de tamanho desconhecido e possa exibir na tela a maior nota. A leitura do valor -1 (flag) indicará o final da leitura dos dados.

nome=input("Escreva o nome do aluno: ")
nota=float(input("Digite a nota ou digite -1 para encerrar: "))

maior_nota = 0 
q_notas = 0

while nota != -1:
  q_notas= q_notas + 1
  nota=float(input("Digite a nota, (ou digite -1 para encerrar): "))
  if nota > maior_nota:
    maior_nota = nota
else:
  print( "Não quis entrar com mais nenhuma nota? Ok! ")
  print ("Foram digitados: " + str(q_notas) + "notas" + "." +  " A maior nota fornecida foi : " + str(maior_nota))








"""
notas = 0
quantidade_numeros = 0
maior = 0

nome = input("Nome: ")
numero = 0

while numero != -1:
  print (quantidade_numeros)
  quantidade_numeros= quantidade_numeros + 1
  if numero > maior:
    maior = numero
  numero = int(input("Digite a nota, " + "(ou digite -1 para sair): "))
print (str(quantidade_numeros) + "jota")
if numero == -1:
    print( "Não quis entrar com mais nenhum número? Ok! Então até a próxima.")
    print( "Foram digitados: " + str(quantidade_numeros) + " números e o maior deles é: " + str(maior) )
  """







"""
print( "Bem-vindo(a) ao programa para somar\num conjunto de números! Vamos começar...\n\n" )

soma = 0
quantidade_números = 0

número = int( input("Insira um número inteiro positivo (ou digite 0 para sair): " ) )
while número != 0:
    soma = soma + número
    quantidade_números = quantidade_números + 1
    número = int( input("Insira um número (ou digite 0 para sair): " ) )

if quantidade_números == 0:
    print( "Não quis entrar com nenhum número?\nOk! Então até a próxima.")
else:
    print( "Foram digitados " + str(quantidade_números) + " números e a soma é: ", str(soma) )
"""