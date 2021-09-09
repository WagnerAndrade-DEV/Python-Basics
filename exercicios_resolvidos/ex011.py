#programa que lê o preço de um produto e monstre seu valor com 5% de desconto

preco = float(input('Digite o valor do produto: R$'))
novo = preco - ((preco * 5) / 100) 

print ('O valor de seu produto com desconto é R${:.2f}' .format(novo))