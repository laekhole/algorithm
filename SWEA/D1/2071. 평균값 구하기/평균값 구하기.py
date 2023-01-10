T=int(input())
sum=0
for t in range(1,T+1):
    numbers=list(map(int,input().split()))
    sum=0
    for i in range(len(numbers)):
        sum+=numbers[i]
    average=round(sum/len(numbers))
    print(f'#{t} {average}')