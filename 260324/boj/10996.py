n = int(input())

out1 = "*" + " *" * ((n - 1) // 2)
out2 = " *" * (n // 2)

for i in range(n * 2):
    if(i % 2):
        print(out2)
    else:
        print(out1)