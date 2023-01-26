N=int(input())
cus=list(map(int,input().split()))
li=[]
for ele in cus:
    if ele not in li:
        li.append(ele)
print(len(cus)-len(li))