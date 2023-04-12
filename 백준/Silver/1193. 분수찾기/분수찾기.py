# 접근 : 각 대각선 line의 분모 분자 합은 line+1이다.
# 홀수 line은 분자가 1씩 줄고 분모가 1씩 늘어나는 형태로 진행하고
# 즉, (line+1-X)/(X)
# 짝수 line은 분모가 1씩 줄고 분자가 1씩 늘어나는 형태로 진행한다.
# 즉, (X)/(line+1-X)


X=int(input())
# cond=True
# 몇번째 대각선 라인인지를 의미
line=1
while X-line>0:
    X-=line
    line+=1
# print(f'line={line},X={X}')


# line이 홀수일 때. 즉, X가 홀수 대각선 라인에 있을 때
if line%2==1:
    # result=(line+1-X)/(X)
    result1=(line+1-X)
    result2=(X)

# line이 짝수일 때. 즉, X가 짝수 대각선 라인에 있을 때
else:
    # line+2 = 분모 분자의 합
    # result=(X)/(line+1-X)
    result1=(X)
    result2=(line+1-X)

print(f'{result1}/{result2}')