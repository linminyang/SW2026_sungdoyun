n = int(input())

data = list(map(int, input().split()))

ans = 0

for i in range(n):
    for j in range(0, i):
        ans += abs(data[i] - data[j]) * 2
print(ans)