#Escreva um programa que converta uma temperatura digitada em C° para F°

celcius = int(input('Digite a temperatura em C°: '))

calculo = 9 * celcius / 5 + 32

print('C {}° corresponde a F {}°' .format(celcius, calculo))