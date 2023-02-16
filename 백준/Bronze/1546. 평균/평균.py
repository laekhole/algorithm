n=int(input())
scores=list(map(int,input().split()))
new_scores=[0 for _ in range(n)]
for _ in range(n):
    new_scores[_]=scores[_]/max(scores)*100
print(sum(new_scores)/n)