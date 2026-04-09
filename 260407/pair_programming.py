arr = list(map(int, input().split()))
n = len(arr)

for i in range (n):
    for j in range (0,n-(i + 1)):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for i in arr: 
    print (i)

for i in range(n):
    print(arr[i])