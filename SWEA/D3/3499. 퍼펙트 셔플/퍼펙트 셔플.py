#SWEA 3499번 퍼펙트 셔플 D3
import math
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    li=list(input().split())
    ans_li=[0 for _ in range(len(li))]
    for i in range((math.ceil(n/2))):
        try:
            ans_li[2*i]=li[i]
            ans_li[2*i+1]=li[i+math.ceil(n/2)]
        except:
            ans_li[2*i]=li[i]
    print(f'#{tc}', end=" ")
    print(*ans_li)