import sys
N, M = map(int, input().split())
arr = dict()
cnt = 0
for _ in range(N):
    s = sys.stdin.readline()
    arr[s] = True
for _ in range(M):
    inp = sys.stdin.readline()
    if inp in arr.keys():
        cnt+=1

print(cnt)