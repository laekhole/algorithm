n = int(input())
lng = list(map(int,input().split()))

li=[[] for i in range(n)]
j=0


for i in range(n):
    try:
        if lng[i]<lng[i+1]:
            li[j].append(lng[i])
            li[j].append(lng[i+1])
        else:
            j+=1
    except:
        pass

for _ in range(n):
    li[_]=list(sorted(set(li[_])))

for __ in range(n):
    try:
        # # print(li[__][0])
        li[__]=abs(li[__][0]-li[__][-1])
    except:
        pass

li2=[]
for ind in range(n):
    if li[ind]!=[]:
        li2.append(li[ind])

try:
    print(max(li2))
except:
    print(0)