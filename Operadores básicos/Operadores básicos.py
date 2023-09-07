numero = input("Informe um número, por favor: ")
print("O valor informado foi: ", numero)

numero_1 = int(input("Informe o primeiro valor, por favor: "))
numero_2 = int(input("Informe o segundo valor, por favor: "))
print("A soma é: ", numero_1 + numero_2)


numero_1 = int(input("Informe o primeiro valor, por favor: "))
numero_2 = int(input("Informe o segundo valor, por favor: "))
numero_3 = int(input("Informe o terceiro valor, por favor: "))
media = (numero_1 + numero_2 + numero_3)/3
print("A media é: ", media)

valor_km = int(input("Informe o valor em km, por favor: "))
valor_cm = valor_km * 100000
print("O valor informado em cm é:", valor_cm, "cm")

def valores(v1,v2,v3):
  resultado = v1 + v2 + v3
  print(resultado)

valores(5,2,8)


"""> Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 a.	o produto do dobro do primeiro com metade do segundo .
 b.	a soma do triplo do primeiro com o terceiro.
 c.	o terceiro elevado ao cubo.
"""

def calculo(valor1, valor2, valor3):
#  a.	o produto do dobro do primeiro com metade do segundo.
  a = (valor1*valor1) * (valor2/2)
#  b.	a soma do triplo do primeiro com o terceiro.
  b = (valor1*3) + valor3
#  c.	o terceiro elevado ao cubo.
  c = valor3**3

  print(f'''
  Questão A: {a}
  Questão B: {b}
  Questão C: {c}
  ''')

calculo(3,2,float(-5))