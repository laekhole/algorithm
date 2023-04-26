A=input()
A_li=[i for i in A]
A=int(A)
B=input()
B_li=[j for j in B]
B=int(B)
# print(A,B)
# print(A,type(A),B[2],type(B[2]))
# print(A*int(B[2]))
# print(int(A)*B[2])
for i in range(3):
    print(A*int(B_li[2-i]))
print(A*B)