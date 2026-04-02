n = int(input())
data = list(map(int, input().split()))

data.sort()
print(f"{data[0]} {data[n - 1]}")