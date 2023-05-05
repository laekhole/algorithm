n=int(input())
x_axis=list()
y_axis=list()
for i in range(n):
    x,y=map(int,input().split())
    x_axis.append(x)
    y_axis.append(y)
print((max(x_axis)-min(x_axis))*(max(y_axis)-min(y_axis)))