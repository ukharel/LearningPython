arr = [1,1,3,4,5,2,2,1,1,1,4,7,8,9,87,5,1,1,1]
max_count=0
for i in range(len(arr)):
    count=0
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            count+=1

    if count>max_count:
        max_count=count
    repeated_num= arr[i]
print(f'Total number of count is: {max_count}')
print(f'Number with most repitation is: {repeated_num}')
      


