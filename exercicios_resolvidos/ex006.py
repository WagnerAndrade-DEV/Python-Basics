#crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um número: '))

d = n * 2 
t = n * 3
r = n ** (1/2) #raiz quadrada, também pode ser feita usando 'pow'

print('A o dobro de {} é {}. \nO triplo de {} é {}. \nA raiz quadrada de {} é {:.2f}' .format(n,d,n,t,n,r))