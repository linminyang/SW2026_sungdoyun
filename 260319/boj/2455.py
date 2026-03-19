ans = 0; v = 0

for i in range(4):
    o, i = input().split()
    i = int(i); o = int(o)
    v = v - o + i
    ans = max(ans, v)

print(ans)