n=int(input())
list_n=list(map(int,str(n)))
sum=0
for i in range(len(list_n)):
    sum+=list_n[i]
print(sum)