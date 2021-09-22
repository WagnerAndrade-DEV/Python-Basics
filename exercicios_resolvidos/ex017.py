#Programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangunlo, calcule e mostre o comprimento da hipotenusa.

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

formula = (cateto_oposto**2 + cateto_adjacente**2) ** (1/2)

print('O valor da hipotenusa é {:.5f}' .format(formula))