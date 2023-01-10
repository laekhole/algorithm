T=int(input())

for t in range(1,T+1):
    numbers=list(map(int,input().split()))
    max=numbers[0]
    for i in range(len(numbers)):
        if max<numbers[i]:
            max=numbers[i]
    print(f'#{t} {max}')