import random
n = int(input())

a = [[0 for _ in range(n)] for _ in range(n)]
output = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = random.randint(1, n * n * 10)

for i in range(n):
    for j in range(n):
        output[i][j] = a[j][i]
"""
for i in range(n):
    for j in range(n):
        print(f"{a[i][j]:4d}", end="")
    print()
"""
for i in range(n):
    for j in range(n):
        print(f"{output[i][j]:4d}", end="")
    print()