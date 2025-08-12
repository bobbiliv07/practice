def array_to_number(array):
    n=len(array)-1
    number=0
    for i in array:
        number=number+i*10**n
        n-=1
    return number
def number_to_array(number):
    digits=[]
    digit=0
    while number > 0:
        digit=number%10
        digits.insert(0,digit)
        number=number//10
    return digits
option=int(input("enter your choice  1 for num-array 2 for array-num :"))
match option :
    case 1:
        number=int(input("enter your number"))
        print(number_to_array(number))
    case 2:
        array=[int(element) for element in input("elements by space: ").split()]

        print(array_to_number(array))
    case _:
        print('not a valid option')




