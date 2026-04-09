swi = [0] * 20000

for i in range(0, 10000):
    x = i
    v = i
    while(v):
        x += v % 10
        v //= 10
    swi[x] = 1
for i in range(1, 10000):
    if(swi[i] == 0):
        print(i)