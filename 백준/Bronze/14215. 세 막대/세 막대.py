a,b,c=map(int,input().split())
len_list=[a,b,c]
arr_list=sorted(len_list)
if max(arr_list)>=sum(arr_list)-max(arr_list):
    arr_list[2]=(sum(arr_list)-max(arr_list))-1
print(sum(arr_list))