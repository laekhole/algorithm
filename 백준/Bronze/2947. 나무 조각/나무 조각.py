inpt=list(map(int,input().split()))
a=inpt[0]

for ind in range(len(inpt)):
    for i in range(len(inpt)):
        try:
            while inpt[i]>inpt[i+1]:
                a=inpt[i+1]
                inpt[i+1]=inpt[i]
                inpt[i]=a
                print(*inpt)
        except:
            pass