#programa que leia um valor em metros e o exiba em mm, cm e km

n = float(input('Digite distancia em metros: '))

mm = n*1000
cm = n*100
km = n/1000

print('{} em milímetros fica {:.1f}. \n{} em centímetros fica {:.1f}. \n{} em quilômetros fica {:.1f}' .format(n, mm, n, cm, n, km))