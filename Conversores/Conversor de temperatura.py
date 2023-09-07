def opcao4(n1):
  print("1 - Fº -> Cº")
  print("2 - Cº -> Fº")

  opcao_escolha = int(input("Informe uma sentença: "))
  conversor_temperatura(n1,opcao_escolha)

def conversor_temperatura(n1, opcao):
  if (opcao == 1):
    resultado = (n1 - 32) * (5 / 9)
    print(f'O valor final da conversão é de: {resultado} Fahrenheit')
  else:
    resultado =  (n1 * (9/5)) + 32
    print(f'O valor final da conversão é de: {resultado} Celsius')

