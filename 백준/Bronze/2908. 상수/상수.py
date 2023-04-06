nums=input().split()

nums_1=[i for i in range(3)]
nums_2=[i for i in range(3)]

for _ in range(3):
    nums_1[_]=nums[0][2-_]
    nums_2[_]=nums[1][2-_]
    
nums_1=list(map(int,nums_1))
nums_2=list(map(int,nums_2))

ans=list(i for i in range(2))
ans[0]=nums_1[0]*100+nums_1[1]*10+nums_1[2]
ans[1]=nums_2[0]*100+nums_2[1]*10+nums_2[2]

if ans[0]>ans[1]:
    print(ans[0])
else:
    print(ans[1])