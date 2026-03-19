arr = ['D', 'C', 'B', 'A', 'A']

a = input()
a = int(a)

if(a < 60) :
    print("F")
else :
    print(arr[(a - 60) // 10])