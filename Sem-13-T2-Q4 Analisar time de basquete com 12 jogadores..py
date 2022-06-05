nome = []
altura = []

for num in range(12):
    num = input()
    nome.append(num)
    a = float(input())
    altura.append(a)


mais_alto = altura.index(max(altura))
media = sum(altura) / len(altura)


print('JOGADOR MAIS ALTO DO TIME')
print(nome[mais_alto])
print(f'{altura[mais_alto]:.2f}')
print('ALTURA MÉDIA DO TIME')
print(f'{media:.2f}')
print('JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')

me = -1
for t in altura:
    me += 1        
    if t > media:        
        print(nome[me])
        print(f'{altura[me]:.2f}')
