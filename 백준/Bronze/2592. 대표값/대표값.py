import sys
li=[0 for z in range(10)]
for i in range(10):
    num=int(sys.stdin.readline())
    li[i]=num
ck_dict={}
order_li=sorted(set(li))
for _ in order_li:
    ck_dict[_]=li.count(_)
max_v=max(ck_dict.values())
rev_dict={v:k for k,v in ck_dict.items()}
print(sum(li)//10, rev_dict.get(max(ck_dict.values())))