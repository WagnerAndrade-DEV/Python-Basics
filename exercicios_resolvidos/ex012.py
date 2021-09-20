#algorimito que leia salario de funcionário e monstre o novo valor com 15% de aumento

antigoSalario = float(input('Digite o valor do salário: R$'))

calculo = antigoSalario + ((antigoSalario * 15) / 100)

print ('O valor do novo salário é R${:.2f}' .format(calculo))
