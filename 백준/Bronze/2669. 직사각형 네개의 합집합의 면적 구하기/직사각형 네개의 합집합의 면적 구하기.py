matrix = [[0] * 100 for _ in range(100 + 1)]

cnt = 0

for i in range(4):
    i, j, x, y = map(int, input().split())
    
    # range(i, x+1)이 아닌 이유: 점 좌표가 아니라 박스 좌표를 구해야 해서
    for a in range(i, x): 
        for b in range(j, y):
            if matrix[a][b] == 0:
                matrix[a][b] += 1
                cnt += 1

print(cnt)