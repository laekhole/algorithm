num_1=list(map(int,input().split()))
num_2=list(map(int,input().split()))
num_3=list(map(int,input().split()))

li_x=[]
li_x.append(num_1[0])
li_x.append(num_2[0])
li_x.append(num_3[0])

li_y=[]
li_y.append(num_1[1])
li_y.append(num_2[1])
li_y.append(num_3[1])

st_x=[]
st_y=[]
for ele in li_x:
    if ele not in st_x:
        st_x.append(ele)
    else:
        st_x.remove(ele)
for ment in li_y:
    if ment not in st_y:
        st_y.append(ment)
    else:
        st_y.remove(ment)

print(*st_x, *st_y)