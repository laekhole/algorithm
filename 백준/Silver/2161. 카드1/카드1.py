# 백준 2161 카드1
N=int(input())
li=[i for i in range(1,N+1)]
ans=[]
# print(li)
for ind in range(N):
    # print(li[0])
    ans.append(li[0])
    try:
        li.pop(0)
        # print(li)
        li.append(li.pop(0))
        # print(li)
    except:
        pass
print(*ans)