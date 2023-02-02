li=[['1'],['0'],['0']]
# print(li[0])
m=int(input())
for _ in range(m):
    a,b=map(int,input().split())
    li[a-1],li[b-1]=li[b-1],li[a-1]
    # print(li)
print(li.index(['1'])+1)