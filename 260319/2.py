a, b, c = int(input().split())

if(a ** 2 + b ** 2 == c ** 2):
    print("직각")
elif(a ** 2 + b ** 2 < c ** 2):
    print("예각")
else:
    print("둔각")
