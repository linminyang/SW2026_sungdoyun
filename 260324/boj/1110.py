n = int(input())

arr = [0] * 101
ans = 0

while (arr[n] == 0):
    arr[n] = 1
    v = (n % 10) * 10 #앞자리
    v += ((n // 10) + (n % 10)) % 10 # 뒷자리
    n = v
    ans += 1

print(ans)