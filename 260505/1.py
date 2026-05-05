import random

n = int(input())

a = [[0 for _ in range(n)] for _ in range(n)]
b = [[0 for _ in range(n)] for _ in range(n)]
c = [[0 for _ in range(n)] for _ in range(n)]
sum = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = random.randint(1, n * n * 10)
        b[i][j] = random.randint(1, n * n * 10)
        #a[i][j] = random.randint(1, 2)
        #b[i][j] = random.randint(1, 2)
        c[i][j] = random.randint(1, n * n * 10)

for i in range(n):
    for j in range(n):
        for k in range(n):
            sum[i][j] += a[i][k] * b[k][j]
        sum[i][j] += c[i][j]
"""
for i in range(n):
    for j in range(n):
        print(f"{a[i][j]:7d}", end="")
    print()
for i in range(n):
    for j in range(n):
        print(f"{b[i][j]:7d}", end="")
    print()
for i in range(n):
    for j in range(n):
        print(f"{c[i][j]:7d}", end="")
    print()
"""
for i in range(n):
    for j in range(n):
        print(f"{sum[i][j]:7d}", end="")
    print()