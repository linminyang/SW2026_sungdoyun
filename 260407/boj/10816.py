n = input()
arr = list(map(int, input().split()))

cnt = {}
for i in arr:
    if((i in cnt) == False):
        cnt[i] = 0
    cnt[i] += 1

m = input()
output = list(map(int, input().split()))
for i in output:
    if (i in cnt):
        print(cnt[i],end=" ")
    else:
        print("0",end=" ")