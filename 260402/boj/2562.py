mv = 0; idx = 0

for i in range(9):
    data = int(input())
    if(mv < data):
        mv = data
        idx = i

print(f"{mv}")
print(f"{idx + 1}")