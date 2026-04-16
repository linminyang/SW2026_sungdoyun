def gcd(a, b):
    if(a % b == 0):
        return b
    else:
        return gcd(b, a % b)

a = int(input())
b = int(input())

print("{} & {} gcd {}".format(a, b, gcd(a, b)))