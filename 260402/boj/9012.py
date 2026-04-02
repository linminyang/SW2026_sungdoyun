tc = int(input())

for i in range(tc):
    arr = input()
    v = 0
    for j in arr:
        if(j == '('):
            v += 1
        else:
            v -= 1
        if(v < 0):
            break
    if(v == 0): print("YES")
    else: print("NO")