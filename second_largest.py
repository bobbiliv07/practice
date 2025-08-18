def second_largest(array):
    n=len(array)
    array.sort()
    for i in range (n-2,-1,-1):
# here we used n-2 because if we write n then n will be length of the array
# which will results in index out of range

        if array[i]!=array[n-1]:
            return array[i]
    return -1
x=[2,1,4,3,5,1,2,6,8,3,6,9,9 ]
# for example x length = 13 but in the for loop if i use range(n) it will gives index out of range
# that is array[13] does not exist
print(second_largest(x))