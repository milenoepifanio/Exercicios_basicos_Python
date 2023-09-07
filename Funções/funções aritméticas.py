# Funções aritmeticas 
def soma(n1,n2):
  resultado = n1+n2
  separar()
  print(f'O valor final é: {resultado}')

def subtracao(n1,n2):
  resultado = n1-n2
  separar()
  print(f'O valor final é: {resultado}')

def divisao(n1,n2):
  resultado = n1/n2
  separar()
  print(f'O valor final é: {resultado}')

def multiplicao(n1,n2):
  resultado = n1*n2
  separar()
  print(f'O valor final é: {resultado}')


  #Funções
def opcao1(n1,n2):
  print("1 - Soma")
  print("2 - Subtração")
  print("3 - Multiplicação")
  print("4 - Divisão")

  opcao_escolha = int(input("Informe uma sentença: "))

  if (opcao_escolha == 1):
    soma(n1,n2)
  elif (opcao_escolha == 2):
    subtracao(n1,n2)
  elif (opcao_escolha == 3):
    multiplicao(n1,n2)
  elif (opcao_escolha == 4):
    divisao(n1,n2)
  else:
    print("Opção invalida")