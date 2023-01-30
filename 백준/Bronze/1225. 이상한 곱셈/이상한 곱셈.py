import sys
A,B=sys.stdin.readline().split()
# print(type(A_li),type(B_li))
# print(A_li,A_li[0])
total=0
A_=0
for _ in A:
    A_+=int(_)
# for i in range(len(A)):
    # total=total+A[i]
    # print(A[i])
for i in range(len(B)):
   total+=A_*int(B[i])
print(total) 