# 백준 2798번 블랙잭
# import sys
# 이제 깨달았는데, split()을 쓰면 list로 변환됨.
N,M=map(int,input().split())

# sys.stdin.readline을 써서 각 값을 int 형변환 시키고 싶었는데 안되더라..
# 구글링해야지.. int()의 사용법을 알아야겠음.
# cards_li=int(sys.stdin.readline().split())
cards_li=list(map(int,input().split()))

# cards의 타입과, 그 원소의 타입을 확인하고 싶었음.
# 인풋에서 map과 input의 타입과 split을 썼을 떄 변화하는 거랑
# list, int의 사용 및 의미를 피동적으로 이해하고 있었다가 더 깊게 이해하는 중..
# print(type(cards),cards)
# print(type(cards_li),type(cards_li[3]))

# M_li는 Max list. list comprehension을 통해 작성. append를 쓰지 않기 위해
# 미리 크기 부여
# M_li=[_ for _ in range(N)]
M_li=[]
# 3장씩 뽑아야 하므로 index error를 막기 위해 range를 설정.
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if cards_li[i]+cards_li[j]+cards_li[k]<=M:
                M_li.append(cards_li[i]+cards_li[j]+cards_li[k])
                # M_li[i]=cards_li[i]+cards_li[j]+cards_li[k]
                # print를 해보니 M_li[i]로 짠 탓에, M_li[0]에서 값이 추가되는 것이 아니라
                # 계속 변하는 것을 알 수 있음.
                # 따라서, append가 나을 듯 함.
                # 그러나 이 문제에서는 상관 없음
                # 상관 있음.
                # i가 같을 때 더 큰 값이 저장될 수도 있는데, 다음 i가 같은 값에서
                # 순서가 눌릴 수 있으므로, 모두 저장하는 append가 맞음.
                # append를 쓰기 싫다면 sorted()로 N을 정렬하고 해야함.
                # print(M_li, i, j, k)
print(max(M_li))