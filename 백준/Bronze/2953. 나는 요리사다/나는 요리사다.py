# 백준 2953번 나는 요리사다
matrix=[list(map(int,input().split())) for _ in range(5)]
mtx=[sum(matrix[i]) for i in range(5)]
print(mtx.index(max(mtx))+1, max(mtx))