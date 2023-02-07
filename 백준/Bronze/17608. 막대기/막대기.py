# 백준 17608번 막대기
import sys

n=int(sys.stdin.readline())
li=[int(sys.stdin.readline()) for tc in range(n)]

# 마지막 막대기보다 커야 하며, 중간에 큰 막대기가 있으면 뒤의
# 덜 큰 막대기는 가려짐
# 따라서, max값을 주고 이 max값을 넘지 못하면 리스트에 추가하지 않기
mx=li[-1]
look_li=[]

for ele in li[::-1]:
    if mx<ele:
        mx=ele
        look_li.append(ele)

print(len(look_li)+1)