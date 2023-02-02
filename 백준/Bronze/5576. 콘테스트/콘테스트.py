# 백준 5576번 콘테스트
li_a=[]
li_b=[]
max_a=[]
max_b=[]
for _ in range(10):
    score=int(input())
    li_a.append(score)
for _ in range(10):
    score=int(input())
    li_b.append(score)
# print(li_a, li_b)
for i in range(3): 
    max_a.append(max(li_a))
    # pop() 함수는 index로 item을 가져오며 삭제. value 넣는 게 아님.
    # value는 remove로
    # max_a.append(li_a.pop(max(li_a)))
    li_a.remove(max(li_a))
    max_b.append(max(li_b))
    li_b.remove(max(li_b))
    # print(max_a)
    # print(li_a)
print(sum(max_a), sum(max_b))