T=int(input())
for tc in range(T):
    num=int(input())
    
    li=[]
    st_li=[]
    for a in range(10):
        st_li.append(str(a))
    # print(st_li)
    for n in range(1,100):
        mtp=num*n
        str_mtp=str(mtp)
        for a in str_mtp:
            if a not in li:
                li.append(a)
            # print(li)
            new_li=sorted(li)
            # print(new_li)
        if new_li==st_li:
            break
    # print(mtp)
    print(f'#{tc+1} {mtp}')