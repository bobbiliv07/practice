def second_largest(array):
    n=len(array)
    array.sort()
    for i in range (n-2,-1,-1):
        if array[i]!=array[n-1]:
            return array[i]
    return -1
x=[2,1,4,3,5,1,2,6,8,3,6,9,9]
print(second_largest(x))