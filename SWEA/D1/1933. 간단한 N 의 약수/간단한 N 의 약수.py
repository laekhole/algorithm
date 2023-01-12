num=int(input())
divnum=[]

for s in range(1,num+1):
    if num%s==0:
        divnum.append(s)
print(*divnum)