k = int(input())

arr = []

for i in range(k):
    data = int(input())
    if(data == 0 and len(arr) != 0):
        arr.pop()
    else:
        arr.append(data)

print(sum(arr))