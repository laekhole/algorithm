# 백준 2455번 지능형 기차
num=0
mxn=0
for tc in range(4):
    f,n=map(int,input().split())
    num-=f
    num+=n
    # print(n,f,num,mxn)
    if num>mxn:
        mxn=num
    # print(n,f,num,mxn)
print(mxn)
