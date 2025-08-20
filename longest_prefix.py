def longestprefix(array):
    prefix=array[0]
    prefix_length=len(prefix)
    for i in array[1:]:
        while prefix != i[0:prefix_length]:
            prefix_length=prefix_length-1
            prefix=prefix[0:prefix_length]
            if prefix_length == 0:
                return ""
            prefix=prefix[0:prefix_length]
    return prefix

x=["vicky","vijay","vinay"]
print(longestprefix(x))