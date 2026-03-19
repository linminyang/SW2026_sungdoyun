#윤년 확인 문제 boj 2753

a = int(input())

if (a % 400 == 0):
    swi = 1
elif (a % 100 == 0):
    swi = 0
elif (a % 4 == 0):
    swi = 1
else :
    swi = 0

print(swi)