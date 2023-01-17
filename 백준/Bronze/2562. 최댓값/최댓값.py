li=[]
for i in range(9):
    num=int(input())
    li.append(num)
st=li[0]
cnt=1
st_num=0
for e in li:
    if st<=e:
        st=e
        st_num=cnt
    cnt+=1
print(st)
print(st_num)