sum=0
for num in range(5):
    score=int(input())
    if score<40:
        score=40
    sum+=score
aver=int(sum/5)
print(aver)