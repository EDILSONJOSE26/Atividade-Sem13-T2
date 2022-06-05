def quantidade(n, lista):
    qtd = 0
    for e in lista:
        if e == n:
            qtd += 1
    return qtd

n = 1
lista1 = []
while n != 0:    
    n = int(input())
    if n > 0:
        lista1.append(n)

numero = int(input())
quant = quantidade(numero, lista1)

print(f'{lista1}')
print(f'{numero}')
print(f'{quant}')
