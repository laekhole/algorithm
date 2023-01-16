qnum=int(input())
li=[]
for i in range(qnum):
    li.append(i)

for e in li:
    if e%2==0:
        li.remove(e)

ans=list(map(int,input().split()))
score=0
sum=0
for i in li:
    if ans[i-1]==1:
        score+=1
        sum+=score
        try:
            if ans[i]==1:
                score+=1
                sum+=score
            elif ans[i]==0:
                score=0
        except:
            pass
    else:
        score=0
        try:
            if ans[i]==1:
                score+=1
                sum+=score
            elif ans[i]==0:
                score=0
        except:
            pass
print(sum)