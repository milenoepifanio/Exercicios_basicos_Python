def modulo(n1,n2):
  resultado = n1%n2
  print(f'O valor final é: {resultado}')

def exponenciacao(n1,n2):
  resultado = n1**n2
  print(f'O valor final é: {resultado}')


def opcao2(n1,n2):
  print("1 - Módulo")
  print("2 - Exponenciação")

  opcao_escolha = int(input("Informe uma sentença: "))

if (opcao_escolha == 1):
    modulo(n1,n2)
elif (opcao_escolha == 2):
    exponenciacao(n1,n2)
else:
    print("Opção invalida")