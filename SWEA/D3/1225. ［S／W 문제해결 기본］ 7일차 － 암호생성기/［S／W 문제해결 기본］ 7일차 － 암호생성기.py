# swea 1225번 암호생성기
# 첫 접근 : pop(0) 이용하여 첫번째 인자 삭제하고 거기에
# for 인자만큼 더하여 뒤에 추가
for tc in range(10):
    if int(input())==tc+1:
        psw=list(map(int,input().split()))
        condition=True
        while condition:
            for i in range(1,6):
                k=0
                # print(psw)
                if psw[0]-i>0:
                    k=int(psw.pop(0)-i)
                    psw.append(k)
                    # print(psw)
                else:
                    psw.pop(0)
                    psw.append(0)
                    condition=False
                    print('#',end="")
                    print(tc+1,end=" ")
                    print(*psw)
                    break