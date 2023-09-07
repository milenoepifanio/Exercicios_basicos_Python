def conversor(n1,n2,opcao):
  if (opcao == 1):
    resultado = n1*n2
    print(f'O valor final da conversão é de: {resultado} reais')
  else:
    resultado = n1/n2
    print(f'O valor final da conversão é de: {resultado} dolares')

def opcao3(n1,n2):
  print("1 - Dólar -> Real")
  print("2 - Real -> Dolar")

  opcao_escolha = int(input("Informe uma sentença: "))
  conversor(n1,n2,opcao_escolha)