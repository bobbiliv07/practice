def array_to_number(array):
    n=len(array)-1
    number=0
    for i in array:
        print(i)
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
x=124




