n=input()
n1=list(map(int,n))
n2=sorted(n1,reverse=True)
print(*n2,sep="")