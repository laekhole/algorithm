n,m=map(int,input().split())
balls=list(range(1,n+1))
for _ in range(m):
    change_1,change_2=map(int,input().split())
    balls[change_1-1],balls[change_2-1]=balls[change_2-1],balls[change_1-1]
print(*balls)