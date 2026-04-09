import math
n = int(input())
m = int(input())

arr = []

for i in range(n, m + 1):
    if(i == 1): continue
    for j in range(2, int(math.sqrt(i)) + 1):
        if(i % j == 0):
            break
    else:
        arr.append(i)

if(len(arr) == 0):
    print("-1")
else:
    print(sum(arr))
    print(arr[0])