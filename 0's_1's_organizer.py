#msot efficient way to organize one and zeros
def organizer(array):
    left=0
    right=len(array)-1
    while left < right:
        if array[left]==0:
            left+=1
        elif array[right]==1:
            right-=1
        else:
            array[left],array[right]=array[right],array[left]
            left+=1
            right-=1
    return array
# the above will return the array in such way that all one and zeros are organized