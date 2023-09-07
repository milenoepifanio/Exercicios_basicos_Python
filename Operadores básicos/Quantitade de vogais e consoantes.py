palavra_informada = input("Informe uma sentença: ")
contagem_vogais = 0
contagem_consoantes = 0
for x in palavra_informada:
  if x in 'aeiou':
    contagem_vogais = contagem_vogais + 1
  else:
    contagem_consoantes = contagem_consoantes + 1
  print(x)

print(f'\n Na frase existem {contagem_vogais} vogais')
print(f'\n Na frase existem {contagem_consoantes} consoantes')