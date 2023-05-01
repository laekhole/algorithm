n=int(input())
cnd=True
share=2
while cnd:
    if n%share==0:
        n/=share
        print(share)
    else:
        share+=1
    if n==1:
        cnd=False