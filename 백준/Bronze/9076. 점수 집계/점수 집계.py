# 백준 9076번 점수 집계
T=int(input())
for tc in range(T):
    score=map(int,input().split())
    # print(score,type(score))
    score=sorted(score)
    new_score=[]
    for ele in score[1:-1]:
        new_score.append(ele)
        # print(new_score)
    if max(new_score)-min(new_score)>=4:
        print("KIN")
    else:
        print(sum(new_score))