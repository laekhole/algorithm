C=int(input())
for _ in range(C):
    sum_score=0
    cnt=0
    scores=list(map(int,input().split()))
    for i in range(1,scores[0]+1):
        sum_score+=scores[i]
    # print(f'sum_score={sum_score}')
    avg_score=sum_score/scores[0]
    # print(f'avg={avg_score}')
    for i in range(1,scores[0]+1):
        if scores[i]>avg_score:
            cnt+=1
    print(f'{cnt/scores[0]*100:.3f}%')