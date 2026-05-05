start = 0
month = int(input())
days = [0,31,28,31,30,31,30,31,30,31,31,30,31]

for i in range(month):
    start = (start + days[i]) % 7

for i in range(start):
    print("   ",end="")

for i in range(1, days[month] + 1):
    print(f"{i:3}",end="")
    if (start + i) % 7 == 0:
        print()