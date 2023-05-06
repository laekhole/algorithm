while True:
    nums=list(map(int,input().split()))
    if nums==[0,0,0]:
        break
    result_list=[]
    for i in nums:
        if i not in result_list:
            result_list.append(i)
    if max(nums)-(sum(nums)-max(nums))>=0:
        print('Invalid')
    else:
        if len(result_list)==3:
            print('Scalene')
        elif len(result_list)==2:
            print('Isosceles')
        else:
            print('Equilateral')