n = int(input())

arr = [0]

for i in range(1, n + 1):  
    v = 99999
    if(i >= 3):
        v = min(v, arr[i - 3] + 1)
    if(i >= 5):
        v = min(v, arr[i - 5] + 1)
    arr.append(v)

if (arr[n] == 99999):
    print("-1")
else:
    print(arr[n])
