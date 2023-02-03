T=int(input())
for tc in range(T):
    N,M=map(int,input().split())
    mat=[list(map(int,input().split())) for i in range(N)]
    total_li=[[] for _ in range(N**2)]
    k=0
    for i in range(N):
        for j in range(N):
            total=0
            for p in range(M):
                try:
                    total+=sum(mat[i+p][j:j+M])
                except:
                    pass
            total_li[k]=total
            k+=1
    print(f'#{tc+1} {max(total_li)}')