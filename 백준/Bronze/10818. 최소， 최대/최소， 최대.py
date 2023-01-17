N= int(input())
nums=[]
in_put=input()
in_put=in_put.split()
# in_put=int(in_put)
for i in in_put:
    nums.append(int(i))

print(min(nums), max(nums))