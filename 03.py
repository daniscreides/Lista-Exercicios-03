#Escreva um programa capaz de ler as notas de 5 alunos onde cada aluno possui 2 notas. Utilize estruturas de repetição para ler os dados de cada aluno e suas 2 notas. O programa deve imprimir o nome de cada aluno e sua média final.


aluno= 1
while aluno <= 5:
  nome = input("Nome do Aluno: ")
  nota1 = float(input("1º Nota: "))
  nota2 = float(input("2º Nota: "))

  media = (nota1 + nota2) / 2 

  print ("Média: " + str(media))
  aluno= aluno + 1
