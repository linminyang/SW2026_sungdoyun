c = int(input())

for i in range(c):
    data = list(map(int, input().split()))
    n = data[0]
    arr = data[1:]
    avg = sum(arr) / n
    cnt = 0
    for i in arr:
        if(i > avg) :
            cnt += 1
    print(f"{cnt/n * 100}", )
