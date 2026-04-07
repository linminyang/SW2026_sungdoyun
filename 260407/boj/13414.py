n, m = input().split()
n = int(n); m = int(m)

dic = {}

for i in range(m):
    a = int(input())
    dic[a] = i

output = []
for key in dic:
    output.append(key + dic[key] * int(1e8))

output.sort()
n = min(n, len(output))
for i in range(n):
    print("{:08d}".format(output[i] % int(1e8)))