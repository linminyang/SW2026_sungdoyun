arr = []

for i in range(10):
    data = int(input())
    arr.append(data%42)

ans = 1
arr.sort()
for i in range(9):
    if(arr[i] != arr[i + 1]):
        cnt += 1

print(cnt)