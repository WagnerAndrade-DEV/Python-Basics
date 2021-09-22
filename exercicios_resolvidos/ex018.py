#Faça um programa que leia um angulo qualquer e monstre na tela o valor do seno, cosseno e tangente deste angulo

from math import radians, sin, cos, tan

angulo = float(input('Digite o valor do angulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(''' O ângulo tem os seguintes valores de: 
Seno {:.2f}
Cosseno {:.2f}
Tangente {:.2f}
'''.format(seno, cosseno, tangente))