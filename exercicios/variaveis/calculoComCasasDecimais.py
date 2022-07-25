'''
    Este é um velho dilema principalmente de linguagens antigas.
    A precisão de casas decimais nos cálculos monetários com mais de duas casas decimais.
    Uma solução simples, sem utilizar o recurso que o Python o proporciona, é:
    -> multiplicação por 1.000 -> decimalParaInteiro ->  cálculo -> inteiroParaDecimal ->
    divisão por 1.000.000 (pois 1.000 x 1.000 dá 1.000.000), assim se obtêm o resultado com
     precisão de casas decimais.
'''

quantFloat = float(input("Digite a quantidade: "))

valorFloat = float(input("Digite o valor: "))

quantInteiro = int(quantFloat * 1000)
valorInteiro = int(valorFloat * 1000)

totalInteiro = quantInteiro * valorInteiro

totalFloat = float(totalInteiro)

totalFloat = totalFloat / 1000000

print("O valor total é: ", totalFloat)