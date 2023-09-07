def separar():
  print(25*'==')

while True:
  separar()
  print("--MENU DE INICIALIZAÇÃO--")
  print("1 - Operações básicas")
  print("2 - Módulo e exponenciação")
  print("3 - Conversor monetário Real - Dólar")
  print("4 - Conversor de temperatura")
  print("Digite 0 para parar")

  separar()
  opcao = int(input("Informe uma sentença: "))

  if (opcao == 1):
    n1 = float(input("Informe o valor 1: "))
    n2 = float(input("Informe o valor 2: "))
    opcao1(n1,n2)
    separar()
  elif (opcao == 2):
    n1 = float(input("Informe o valor 1: "))
    n2 = float(input("Informe o valor 2: "))
    opcao2(n1,n2)
    separar()
  elif (opcao == 3):
    n1 = float(input("Informe o valor da cotação: "))
    n2 = float(input("Informe o valor que você precisa converter: "))
    opcao3(n1,n2)
    separar()
  elif (opcao == 4):
      n1 = float(input("Informe o valor 1: "))
      opcao4(n1)
      separar()
  elif (opcao == 0):
    break;
  else:
    print("Opção invalida")
    separar()