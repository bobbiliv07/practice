def moving_zeros(array):
    size=len(array)
    count=0
    for i in range(size):
        if array[i]!=0:
            array[count]=array[i]
            count+=1

    while count < size :
        array[count]=0
        count+=1
    return array
a=[1, 2, 0, 4, 3, 0, 5, 0]
print(moving_zeros(a))

