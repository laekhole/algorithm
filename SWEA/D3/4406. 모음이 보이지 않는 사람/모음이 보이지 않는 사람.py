vowel='aeiou'
T=int(input())
for tc in range(1,T+1):
    word=input()
    ans=[]
    for ele in word:
        if ele not in vowel:
            ans.append(ele)
    print(f'#{tc}',end=" ")
    print(*ans,sep="")