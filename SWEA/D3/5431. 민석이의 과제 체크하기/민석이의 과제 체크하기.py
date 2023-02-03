# swea 민석이의 과제 체크하기 D3
T=int(input())
for tc in range(T):
    N,K=map(int,input().split()) # map으로 N,K 선언
    # map으로 선언한 게 변수 하나면 type map으로 기록 되고,
    # 그 때의 hash값이 출력되는데 각 변수에 맞게 집어넣어서 int로 출력.
    # print(N,K,type(N),type(K))
    submit_li=sorted(list(map(int,input().split())))
    total_li=[i+1 for i in range(N)]
    # print(total_li)
    # print(submit_li)
    ans_li=[]
    # 중복 제거 만드는 for 구문 응용
    for ele in total_li:
        if ele not in submit_li:
            ans_li.append(ele)
    # print(type(tc))
    print('#',end="")
    print(tc+1,end=" ")
    print(*ans_li)