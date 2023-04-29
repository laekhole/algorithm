n=int(input())
nums=list(map(int,input().split()))
ans=list()
for i in nums:
    cnd=True
    cnt=0
    a=1
    while cnd:
        rst=i/a
        rst_int=int(i/a)
        if rst==rst_int:
            cnt+=1
        a+=1
        if a>i:
            cnd=False
    if cnt==2:
        ans.append(i)
print(len(ans))