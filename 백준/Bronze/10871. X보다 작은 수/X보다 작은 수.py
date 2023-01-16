N,X=map(int,input().split())
A=list(map(int,input().split()))
new_A=[]
for e in A:
    if e<X:
        new_A.append(e)

print(*new_A)
# for e in new_A:
#     print(e, end=" ")