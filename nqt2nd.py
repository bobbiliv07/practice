def finding_largest(array):
    if not array:
        return []
    current_sum=array[0]
    current_sub=[array[0]]
    highest_sum=array[0]
    highest_sub=[array[0]]
    for i in range(1,len(array)):
        if array[i]>array[i-1]:
            current_sum+=array[i]
            current_sub.append(array[i])
        else:
            if current_sum > highest_sum:
                highest_sum=current_sum
                highest_sub=current_sub
            current_sum=array[i] # written array[0] before
            current_sub=[array[i]] # written [array[0]] before
        if current_sum>highest_sum:
            highest_sub=current_sub
    return highest_sub
input_list = [1,2,3,5,1,2,3]
result = finding_largest(input_list)
print(sum(result))
