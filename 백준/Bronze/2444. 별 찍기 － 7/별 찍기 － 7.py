# 백준 2444 별 찍기-7
n=int(input())
for i in range(n-1):
    print((n-1-i)*' '+(i*'*'),end="")
    print('*',end="")
    print((i*'*'))
for i in range(n-1,-1,-1):
    print((n-1-i)*' '+(i*'*'),end="")
    print('*',end="")
    print((i*'*'))