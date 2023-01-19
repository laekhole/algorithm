inpt_li=[]
for rep in range(7):
    inpt=int(input())
    inpt_li.append(inpt)

odd_li=[]
for ele in inpt_li:
    if ele%2==1:
        odd_li.append(ele)
        if odd_li==0:
            odd_li.append(-1)

total=0
for ment in odd_li:
    total+=ment
try:
    print(f'{total}\n{min(odd_li)}')
except:
    print(-1)