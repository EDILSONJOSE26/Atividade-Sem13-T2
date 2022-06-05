def quantidade(lista):
    qtd = 0
    for e in lista:
        qtd += 1
    return qtd

def inverter(lista):
    count = 0    
    lista_invertida = []
    indice = len(lista) - 1
    while indice >= 0:
        lista_invertida.append(lista[indice])
        indice -= 1
    return lista_invertida

def menor(lista):
    menor = lista[0]
    for e in lista:    
        if e < menor:
            menor = e
    return menor

def maior(lista):
    maior = lista[0]
    for e in lista:
        if e > maior:
            maior = e
    return maior

def somar(lista):
    soma = 0
    for e in lista:
        soma += e
    return soma


lista1 = []
n = 1
while n != 0:
    n = int(input(''))    
    if n > 0:
        lista1.append(n)

print(f'{lista1}')
print(f'{quantidade(lista1)}')
print(f'{inverter(lista1)}')
print(f'{menor(lista1)}')
print(f'{maior(lista1)}')
print(f'{somar(lista1)}')
