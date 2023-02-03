# swea 조교의 성적 매기기
T=int(input())
for tc in range(T):
    N,K=map(int,input().split())
    # mid,fin,hw=map(int,input().split()) # input 우선순위를 잘 몰라서.. 실패.
    li=[list(map(int,input().split())) for _ in range(N)]
    score=0
    grade_li=[]
    for _ in range(N):
        score=li[_][0]*0.35+li[_][1]*0.45+li[_][2]*0.2
        grade_li.append(score)
    # print(li)
    # sorted 정렬 reverse하고 싶은데 할 줄 모르겠네... 쩝.
    rank_li=sorted(grade_li)
    # print(grade_li)
    # print(rank_li)
    # print(grade_li[K-1])
    # print((rank_li.index(grade_li[K-1])+1))
    # print((rank_li.index(grade_li[K-1])+1)/N)
    rank=(rank_li.index(grade_li[K-1])+1)/N
    if rank>0.9:
        print(f'#{tc+1} A+')
    elif rank>0.8:
        print(f'#{tc+1} A0')
    elif rank>0.7:
        print(f'#{tc+1} A-')
    elif rank>0.6:
        print(f'#{tc+1} B+')
    elif rank>0.5:
        print(f'#{tc+1} B0')
    elif rank>0.4:
        print(f'#{tc+1} B-')
    elif rank>0.3:
        print(f'#{tc+1} C+')
    elif rank>0.2:
        print(f'#{tc+1} C0')
    elif rank>0.1:
        print(f'#{tc+1} C-')
    else:
        print(f'#{tc+1} D0')