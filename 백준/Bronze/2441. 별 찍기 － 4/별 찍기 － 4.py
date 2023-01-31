N=int(input())
star='*'
spc=' '
M=N
while N>0:
    print(' '*(M-N),sep="",end="")
    print('*'*N)
    N-=1