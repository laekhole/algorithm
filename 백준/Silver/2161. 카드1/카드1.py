N=int(input())
li=[i for i in range(1,N+1)]
ans=[]
for ind in range(N):
    ans.append(li[0])
    try:
        li.pop(0)
        li.append(li.pop(0))
    except:
        pass
print(*ans)