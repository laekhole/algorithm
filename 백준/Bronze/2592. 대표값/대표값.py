# 백준 2592번 대표값
import sys
li=[0 for z in range(10)]
for i in range(10):
    num=int(sys.stdin.readline())
    li[i]=num
    # print(num, li)
ck_dict={}
order_li=sorted(set(li))
for _ in order_li:
    ck_dict[_]=li.count(_)
# print(ck_dict, max(ck_dict.values()))
# print(sum(li)//10)
# print(max(ck_dict.values()))
max_v=max(ck_dict.values())
max_k=[k for k,v in ck_dict.items() if v==max_v]
# print(*max_k,max_v)
print(sum(li)//10, *max_k)