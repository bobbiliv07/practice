# this is the code for finding the longest sequence followed by 1
# for any other number replace 1 with the target number
def sequence(array):
    size=len(array)
    current_count=0
    highest_count=0
    for i in range(size):
        if array[i]==1:
            current_count+=1
            highest_count=max(highest_count,current_count)
        else:
            current_count=0
    highest_count=max(highest_count,current_count)
    return highest_count
array=[1,1,0,1,1,1]
print(sequence(array))