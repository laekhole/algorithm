start=input()
li=[]
while start=='고무오리 디버깅 시작':
    mes=input()
    # print(type(mes),mes)
    if mes=="문제":
        li.append(mes)
    elif mes=="고무오리":
        if len(li)!=0:
            li.pop()
        elif len(li)==0:
            li.append(mes)
            li.append(mes)
    if mes=="고무오리 디버깅 끝":
        if len(li)==0:
            print("고무오리야 사랑해")
            break
        else:
            print("힝구")
            break