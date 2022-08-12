"""Escreva um algoritmo capaz de simular (uma parte) do uso de um menu de operações simples para um sistema de caixa automático bancário. O programa deve iniciar exibindo o menu abaixo. O usuário, então, pode escolher uma opção de uso—que apenas deverá ser impressa na tela (e.g., "Você escolheu a opção 1, sacar!")—e o programa deve retornar ao menu principal. Se teclar 0 (zero), o programa deve sair do menu e encerrar o atendimento do usuário. A fim de tentar reduzir longas filas de espera, neste programa bancário, o usuário pode realizar, no máximo, três operações em sequência. Caso tente executar mais, o programa deve alertar que o número máximo de operações foi utrapassado, sair do menu e encerrar o atendimento.
* * * * * * * * * * * * 
Terminal de atendimento
Banco do Nordeste - BNE
* * * * * * * * * * * * 
1- Saque
2- Extrato
3- Depósito
4- Transferência
* * * * * * * * * * * * 
0- Encerrar atendimento
"""








for i in range (3): 
  
  print("-----------------------------------------------")
  print("TERMINAL DE ATENDIMENTO BANCO DO NORDESTE - BNE")
  print("-----------------------------------------------")
  print("-----> SELECIONE ABAIXO A OPÇÃO DESEJADA <-----")
  print("-----------------------------------------------")
  print("                    MENU                       ")
  print("-----------------------------------------------")
  print("1- Saque ")
  print("2- Extrato ")
  print("3- Depósito ")
  print("4- Transferência ")
  print("0- Encerrar antendimento ")

  menu=float(input())
  
  if menu==1:
    print ("Você selecionou a opção 1, SAQUE! ")
    
  elif menu==2:
    print ("Você selecionou a opção 2, EXTRATO! ")
    
  elif menu==3: 
    print ("Você selecionou a opção 3, DEPÓSITO! ")

  elif menu==4: 
    print ("Você selecionou a opção 4, TRANSFERÊNCIA! ")
    
  else:
    print("Você encerrou o atendimento! ")
    break

if menu < 0 or menu > 4:
  print ("OPÇÃO INVÁLIDA!")






