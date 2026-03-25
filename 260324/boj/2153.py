import math

arr = input()
sum = 0
for i in arr:
    if(i <= "Z"):
        sum += ord(i) - ord('A') + 27
    else:
        sum += ord(i) - ord('a') + 1

for i in range(2, int(math.sqrt(sum)) + 1):
    if(sum % i == 0):
        print("It is not a prime word.")
        break
else :
    print("It is a prime word.")