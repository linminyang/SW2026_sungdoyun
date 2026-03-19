x = int(input())
y = int(input())

if(x > 0 and y > 0):
    swi = 1
elif(x < 0 and y > 0):
    swi = 2
elif(x < 0 and y < 0):
    swi = 3
else :
    swi = 4

print(swi)