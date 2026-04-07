n = int(input())

member = set()

for i in range(n):
    name, move = input().split()
    if(move == "enter"):
         member.add(name)
    else:
         member.discard(name)

output = []
for i in member:
     output.append(i)

output.sort()
output.reverse()

for i in output:
     print(i)