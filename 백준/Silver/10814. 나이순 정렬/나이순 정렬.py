n=int(input())
li=[[0 for i in range(2)] for i in range(n)]
for i in range(n):
    li[i]=list(input().split())
    li[i][0]=int(li[i][0])
answer=sorted(li, key=lambda x : (x[0]))
for i in range(n):
    print(answer[i][0],answer[i][1])