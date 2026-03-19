for i in range(3):
    arr = ['D', 'C', 'B', 'A', 'E']
    a, b, c, d = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    sum = a + b + c + d
    print(arr[sum])
    