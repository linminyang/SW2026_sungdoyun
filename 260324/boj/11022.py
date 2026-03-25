t = int(input())

for i in range(t):
    a, b = input().split()
    print("Case #{I}: {A} + {B} = {S}".format(I = i + 1, A = int(a), B = int(b), S = int(a) + int(b)))