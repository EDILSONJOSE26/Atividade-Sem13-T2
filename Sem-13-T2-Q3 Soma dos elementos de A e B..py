a = []
b = []
cont = 0
for c in range(1, 41):
    ele = int(input().strip())
    cont+=1
    if cont <= 20:
        a.append(ele)
    else:
        b.append(ele)


c = []
for i in range(20):
    c.append(a[i]+b[i])

print(f'{a[:]}')
print(f'{b[:]}')
print(c)
