TC=int(input())
for tc in range(1,TC+1):

    s=input()
    ss=set(s)
    # print(ss)
    li_s=list(ss)
    if len(ss)!=2:
        print(f'#{tc} No')
    elif len(li_s)==2:
        if s.count(li_s[0])==2:
            if s.count(li_s[1])==2:
                print(f'#{tc} Yes')