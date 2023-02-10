# SWEA 1208번 Flatten D3
T=10
for tc in range(1,T+1):
    times=int(input())
    li=list(map(int,input().split()))
    for _ in range(times):
        max_index=li.index(max(li))
        min_index=li.index(min(li))
        li[max_index]-=1
        li[min_index]+=1
        # print(max(li),min(li))
        ans=max(li)-min(li)
    print(f'#{tc} {ans}')