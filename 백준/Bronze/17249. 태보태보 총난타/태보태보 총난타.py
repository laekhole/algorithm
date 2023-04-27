capt=input()
pnch="@"
fce="(^0^)"
cnt_l=0
cnt_r=0
for e in capt:
    if e=='@':
        cnt_l+=1
    elif e=="(":
        break
for e in capt[::-1]:
    if e=='@':
        cnt_r+=1
    elif e==")":
        break
print(cnt_l, cnt_r)