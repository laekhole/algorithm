A=B=1
while A!=0 and B!=0:
    A,B=map(int,input().split())
    if A==0:
        break
    else:
        print(A+B)