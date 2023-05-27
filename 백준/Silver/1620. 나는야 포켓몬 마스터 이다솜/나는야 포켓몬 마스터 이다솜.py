import sys

n,m=map(int,sys.stdin.readline().split())
poke={}
poke_reverse={}
for i in range(1,n+1):
    ans=sys.stdin.readline().rstrip()
    poke[i]=ans
    poke[ans]=i
for i in range(m):
    ans=sys.stdin.readline().rstrip()
    if ans.isdigit():
        print(poke[int(ans)])
    else:
        print(poke[ans])