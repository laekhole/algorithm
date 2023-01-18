# 10809번 알파벳 찾기
word=input()
word=list(word)
cnt=0
a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=v=w=x=y=z=-1

cd="abcdefghijklmnopqrstuvwxyz"
ck=[]
for ment in cd:
    ck.append(ment)

li=[]
for _ in word:
    if _ not in li:
        li.append(_)
    else:
        li.append(1)
for ele in li:
    if ele=='a':
        a=cnt
    elif ele=='b':
        b=cnt
    elif ele=='c':
        c=cnt
    elif ele=='d':
        d=cnt
    elif ele=='e':
        e=cnt
    elif ele=='f':
        f=cnt
    elif ele=='g':
        g=cnt
    elif ele=='h':
        h=cnt
    elif ele=='i':
        i=cnt
    elif ele=='j':
        j=cnt
    elif ele=='k':
        k=cnt
    elif ele=='l':
        l=cnt
    elif ele=='m':
        m=cnt
    elif ele=='n':
        n=cnt
    elif ele=='o':
        o=cnt
    elif ele=='p':
        p=cnt
    elif ele=='q':
        q=cnt
    elif ele=='r':
        r=cnt
    elif ele=='s':
        s=cnt
    elif ele=='t':
        t=cnt
    elif ele=='u':
        u=cnt
    elif ele=='v':
        v=cnt
    elif ele=='w':
        w=cnt
    elif ele=='x':
        x=cnt
    elif ele=='y':
        y=cnt
    elif ele=='z':
        z=cnt
    cnt+=1
print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)