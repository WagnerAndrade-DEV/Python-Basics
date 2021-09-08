#conversor de real em dolar (dolar cotado em 5,17 no dia em que este programa foi escrito)

real = float(input('Digite o valor em real: R$'))
dolar = real / 5.17

if real > 1:
    print('R${} reais equivalem a ${:.2f} dolares' .format(real, dolar))

elif real == 1:
    print('R${} real equivale a ${:.2f} dolar' .format(real, dolar))

else:
    print('Digite um valor válido')