import math

target = int(input())

for i in range(2, int(math.sqrt(target))):
    if(target % i == 0):
        print("It's not prime number")
        break
else:
    print("It's prime number")