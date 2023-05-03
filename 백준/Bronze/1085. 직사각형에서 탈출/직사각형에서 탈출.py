x,y,w,h=map(int,input().split())
length_min=list()
if w-x>x:
    length_min.append(x)
else:
    length_min.append(w-x)
if h-y>y:
    length_min.append(y)
else:
    length_min.append(h-y)
# print(length_min,min(length_min))
print(min(length_min))