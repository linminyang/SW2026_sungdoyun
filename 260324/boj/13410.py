n, k = input().split()
n = int(n); k = int(k)

arr = []

for i in range(k):
    v = n * (i + 1)
    v = str(v)
    v = v[::-1] # 문자열 뒤집기
    arr.append(int(v))

print(max(arr))
