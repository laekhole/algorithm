T=int(input())
for tc in range(1,T+1):
    str_date=input()
    new_date=[]
    for a in str_date:
        new_date.append(a)

    date=int(str_date)
    year=date//10000
    month=(date//100)%year
    day=date%100
    
    py=(new_date[0]+new_date[1]+new_date[2]+new_date[3])
    pm=(new_date[4]+new_date[5])
    pd=(new_date[6]+new_date[7])
    
    clear=f'#{tc} {py}/{pm}/{pd}'
    fail=f'#{tc} -1'


    if month>12:
        print(fail)
    elif month==0:
        print(fail)
        continue
    if month==2:
            if day>29:
                print(fail)
            else:
                print(clear)
    else:
        if month==4 or 6 or 9 or 11:
            if day>31:
                print(fail)
        if month==1 or 3 or 5 or 7 or 8 or 10 or 12:
            if day>32:
                print(fail)
        if day==0:
            print(fail)
        print(clear)       