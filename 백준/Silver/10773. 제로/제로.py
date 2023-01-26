T=int(input())
li=[]
for tc in range(T):
    num=int(input())
    if num==0:
        li.pop()
    else:
        li.append(num)
    # print(li)
total=0
for ele in li:
    total+=ele
    # print(total)
print(total)