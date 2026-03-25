n, x = input().split()
n = int(n); x = int(x)

arr = list(map(int, input().split()))

for i in arr:
    if(i < x):
        print(i, end=" ")