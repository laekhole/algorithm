T=int(input())
for e in range(T):
    try:
        cases=int(input())
        nums=list(map(int,input().split()))
        total=0
        for e in nums:
            total+=e
        print(total)
    except:
        pass