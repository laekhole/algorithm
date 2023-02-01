N,M=map(int,input().split())
cards_li=list(map(int,input().split()))
M_li=[]
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if cards_li[i]+cards_li[j]+cards_li[k]<=M:
                M_li.append(cards_li[i]+cards_li[j]+cards_li[k])
print(max(M_li))