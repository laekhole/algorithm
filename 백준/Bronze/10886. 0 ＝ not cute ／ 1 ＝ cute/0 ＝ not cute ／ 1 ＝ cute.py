cnt=0
T=int(input())
for tc in range(T):
    ans=int(input())
    cnt+=ans
if cnt/T>=0.5:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")