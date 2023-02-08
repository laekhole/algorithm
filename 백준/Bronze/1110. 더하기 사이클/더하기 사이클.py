n=input()
nn=n
if len(nn)==1:
    n='0'+nn
    nn=n
cnt=0
while True:
    nn=nn[-1]+str(int(nn[0])+int(nn[1]))[-1]
    cnt+=1
    if nn==n:
        break
print(cnt)