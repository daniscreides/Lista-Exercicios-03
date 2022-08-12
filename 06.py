"""Faça um programa que, para um número desconhecido de pessoas:
leia a idade de cada pessoa, sendo que a leitura da idade -1 (flag) indica o final da leitura dos dados e não deve ser considerada;
ao final, calcule e escreva a quantidade de pessoas;
calcule e escreva a idade média do grupo;

"""

idade=0
quantidades_pessoas=0
maior_idade=0
menor_idade=999
idade_media=0
total_idade=0

while idade != -1: 
  idade=(int(input("Digite Idade: ")))
  if idade == -1:
    break
  total_idade = total_idade + idade
  if idade >= maior_idade:
    maior_idade= idade
  if idade <= menor_idade:
    menor_idade = idade
  quantidades_pessoas= quantidades_pessoas+1  
idade_media = total_idade/quantidades_pessoas
print ("Idade média de pessoas entrevistadas: " + "{:.0f}".format(idade_media))
print ("Quantidade de pessoas entrevistadas: " + "{:.0f}".format(quantidades_pessoas))
print ("Maior idade: " + str(maior_idade))
print ("Menor idade: " + str(menor_idade))