#faça um programa que leia algo digitado e monstre na tela todas suas informações

a = input('Digite algo: ')

print('O tipo primitivo de {} é {}'.format(a, type(a)))
print('{} só tem espaços? {}'.format(a, a.isspace()))
print('{} é um número? {}'.format(a, a.isnumeric()))
print('{} é alfabético? {}'.format(a, a.isalpha()))
print('{} é alfanumérico? {}'.format(a, a.isalnum()))
print('{} está em maiúsculas? {}'.format(a, a.isupper()))
print('{} está em minúsculas? {}'.format(a, a.islower()))
print('{} está capitalizada? {}'.format(a, a.istitle()))