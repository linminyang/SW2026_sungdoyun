n, m = input().split()
n = int(n); m = int(m)

arr = set()

for i in range(n):
    a = input()
    arr.add(a)

output = []
for j in range(m):
    a = input()
    if(a in arr):
        output.append(a)

output.sort()
print(len(output))
for i in output:
    print(i)    