n = int(input())

cnt = {}
mv = 0; ans = ""

for i in range(n):
    a = input()
    if(a in cnt):
         cnt[a] += 1
    else:
         cnt[a] = 1
    if(mv < cnt[a]):
         mv = cnt[a]
         ans = a
    elif(mv == cnt[a] and ans > a):
         ans = a
    
print(ans)