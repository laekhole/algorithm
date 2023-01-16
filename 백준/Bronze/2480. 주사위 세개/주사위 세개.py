# 2480번
dice=list(map(int,input().split()))
dice.sort()
#1
if dice[0]==dice[1] and dice[1]==dice[2]:
    print(10000+dice[0]*1000)
#2
elif dice[0]==dice[1] or dice[1]==dice[2]:
    print(1000+dice[1]*100)
#3
elif dice[0]!=dice[1] and dice[1]!=dice[2]:
    print(dice[2]*100)
