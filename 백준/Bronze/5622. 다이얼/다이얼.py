dialog={
'A':2,'D':3,'G':4,'J':5,'M':6,'P':7,'T':8,'W':9,
'B':2,'E':3,'H':4,'K':5,'N':6,'Q':7,'U':8,'X':9,
'C':2,'F':3,'I':4,'L':5,'O':6,'R':7,'V':8,'Y':9,
                              'S':7,      'Z':9
}
li=[]
inpt=input().upper()
for i in range(len(inpt)):
    # print(dialog[inpt[i]])
    li.append(dialog[inpt[i]])
# print(li)
total=0
for j in range(len(inpt)):
    total+=int(li[j]+1)
print(total)