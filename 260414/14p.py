def haoi(n, start, end, mid):
    if(n == 1):
        print("1 : {} -> {}".format(start, end))
    else:
        haoi(n - 1, start, mid, end)
        print("{} : {} -> {}".format(n, start, end))
        haoi(n - 1, mid, end, start)

haoi(int(input()), 1, 3, 2)