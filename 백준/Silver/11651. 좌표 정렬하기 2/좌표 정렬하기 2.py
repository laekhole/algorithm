import sys
n = int(sys.stdin.readline())
li=[[0 for i in range(2)] for i in range(n)]
for i in range(n):
    li[i][0],li[i][1]=map(int,sys.stdin.readline().split())
answer=sorted(li, key=lambda x : (x[1], x[0]))
for i in range(n):
    print(answer[i][0],answer[i][1])