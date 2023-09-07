"""> Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
 a)	salário bruto.
 b)	quanto pagou ao INSS.
 c)	quanto pagou ao sindicato.
 d)	o salário líquido.
 e)	calcule os descontos e o salário líquido, conforme a tabela abaixo:
"""

def Calculo_salarial(ValorPorHora, NumeroHorasTrabalhadas):
  ValorBruto = ValorPorHora * NumeroHorasTrabalhadas
  ValorIR = ValorBruto * (11/100)
  ValorINSS = ValorBruto * (8/100)
  ValorSindicado = ValorBruto * (5/100)
  SalarioLiquido = ValorBruto - ValorIR - ValorINSS - ValorSindicado

  print(f'''
  Valor Bruto: {ValorBruto}
  Valor do Imposto de Renda: {ValorIR}
  Valor do INSS: {ValorINSS}
  Valor do Sindicado: {ValorSindicado}
  Valor do Salário Líquido: {SalarioLiquido}
  ''')

Calculo_salarial(150, 160)
