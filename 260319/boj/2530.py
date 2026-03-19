h, m, s = input().split()
h = int(h)
m = int(m)
s = int(s)
sum = int(input())

h += sum // 3600
sum %= 3600
m += sum // 60
sum %= 60
s += sum

if(s >= 60):
    s -= 60
    m += 1
if(m >= 60):
    m -= 60
    h += 1
if(h >= 24):
    h %= 24

print(h, m, s)