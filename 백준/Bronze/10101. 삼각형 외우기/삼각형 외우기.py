A=int(input())
B=int(input())
C=int(input())

li=[A,B,C]
li=sorted(li)
ans=[]
for ele in li:
    if ele not in ans:
        ans.append(ele)
if len(ans)==1:
    if A==60:
        print('Equilateral')
    else:
        print('Error')
elif len(ans)==2:
    if sum(li)==180:
        print("Isosceles")
    else:
        print('Error')
elif len(ans)==3:
    if sum(li)==180:
        print("Scalene")
    else:
        print('Error')