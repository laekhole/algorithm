T=int(input())
for tc in range(T):
    rep,word=input().split()
    # print(word)
    rep=int(rep)
    # print(type(rep))
    ans=[]
    for i in word:
        ans.append(i*rep)
    # print(ans)
    print(*ans,sep='')