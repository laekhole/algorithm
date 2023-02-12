T=int(input())
li=[]
nums=[[0] for _ in range(101)]
mx=0
mx_li=[]
for tc in range(1,T+1):
    t=int(input())
    scores=list(map(int,input().split()))
    for ele in scores:
        if ele not in li:
            li.append(ele)
        elif ele in li:
            nums[100-ele]=scores.count(ele)
    # print(nums)
    print(f'#{tc} {100-nums.index(max(nums))}')