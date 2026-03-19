a = input()

if(a == 0):
    print("0")

l = len(a)
start = ""
output = []
swi = 0

for i in range(l):
    v = int(a[i])
    if(swi):
        output.append(str(v // 4))
        output.append(str((v % 4) // 2))
        output.append(str(v % 2))
    else:
        if(v // 4):
            start += "1"
            swi = 1
        if((v % 4) // 2):
            start += "1"
        elif swi:
            start += "0"
        start += str(v % 2)
        swi = 1

print(start+"".join(output))