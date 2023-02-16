T=int(input())
for _ in range(T):
    cnt=0
    score=0
    quiz=input()
    for _ in range(len(quiz)):
        if quiz[_]=='O':
            cnt+=1
            score+=cnt
        elif quiz[_]=='X':
            cnt=0
    print(score)