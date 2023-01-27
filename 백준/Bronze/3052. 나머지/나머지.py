# 백준 3052번 나머지
li=[_ for _ in range(10)]
for i in range(10):
    inp=int(input())
    li[i]=(inp%42)
ans=[]
for ele in li:
    if ele not in ans:
        ans.append(ele)
print(len(ans))
