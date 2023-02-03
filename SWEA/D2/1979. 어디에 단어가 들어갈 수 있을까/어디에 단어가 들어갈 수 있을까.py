from pprint import pprint
T=int(input())
for tc in range(T):
    N,K=map(int,input().split())
    li=[list(map(int,input().split())) for _ in range(N)]
    transform_li=[([0]*N) for _ in range(N)]
    for p in range(N):
        for q in range(N):
            transform_li[p][q]=li[q][p]
    # pprint(transform_li)
    cnt=0
    for i in range(N):
        for j in range(N-K+1):
                if sum(li[i][j:j+K])==K:
                    # print(i,j,K)
                    try:
                        if sum(li[i][j:j+K+1])>K:
                            pass
                        elif sum(li[i][j-1:j+K])>K:
                            pass
                        else:
                            # print(f'i={i},j={j},K={K}')
                            # print('li')
                            cnt+=1
                    except:
                        cnt+=1
                if sum(transform_li[i][j:j+K])==K:
                    try:
                        if sum(transform_li[i][j:j+K+1])>K:
                            pass
                        elif sum(transform_li[i][j-1:j+K])>K:
                            pass
                        else:
                            # print(f'i={i},j={j},K={K}')
                            # print('transform_li')
                            cnt+=1
                    except:
                        cnt+=1
    print(f'#{tc+1} {cnt}')