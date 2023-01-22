hur,minte=map(int,input().split())
cost=int(input())
# print(hur,minte,cost)
# print(type(hur),type(minte),type(cost))


while minte+cost>=60:
    hur+=1
    minte+=cost-60
    cost=0

minte+=cost

if hur>23:
    hur-=24
print(hur, minte)