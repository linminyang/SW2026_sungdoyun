arr = input()
l = len(arr)

output = []

v = 0
for i in range(l):
    swi = (l - i) % 3
    v = v * 2 + int(arr[i])

    if (swi == 1):
        output.append(str(v))
        v = 0

print("".join(output))