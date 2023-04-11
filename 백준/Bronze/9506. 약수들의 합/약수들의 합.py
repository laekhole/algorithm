while True:
    n=int(input())
    if n==-1:
        break
    divided_list=list()
    # 큰 수부터 약분하면 약수가 오름차순 배치된다.
    for i in range(n,1,-1):
        if n/i==int(n/i):
            divided_list.append(n//i)
    # print(divided_list)
    # 약수의 합 변수 생성
    divided_sum=0
    for i in divided_list:
        divided_sum+=i
    # f string을 이용하여 출력
    if divided_sum!=n:
        print(f'{n} is NOT perfect.')
    else:
        print(f'{n} = ',end="")
        for i in divided_list:
            print(f'{i}',end="")
            if i==divided_list[-1]:
                print("")
                break
            print(" + ",end="")