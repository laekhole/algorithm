T=int(input())
li=[25,10,5,1]

for tc in range(T):
    ans=[]
    mon=int(input())
    for i in li:
        ans.append(mon//i)
        mon%=i
    print(*ans)