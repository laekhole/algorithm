n,b=input().split()
b=int(b)
# print(n,b)
notation="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result=0
for _ in range(len(n)):
    result+=notation.index(n[_])*(b**(len(n)-1-_))
print(result)