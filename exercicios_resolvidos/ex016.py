#Crie um programa que lia um número Real qualquer pelo teclado e mostre na tela sua porção inteira

from math import trunc

num = float(input('Digite um valor: '))

print('O valor digitado foi {} e sua porção inteira é {}' .format(num, trunc(num)))