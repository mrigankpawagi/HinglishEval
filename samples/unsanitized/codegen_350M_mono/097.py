
def multiply(a, b):
    """
    Do integers ka input lekar unke unit digits ka product return karega ye function.
    Maan lo ki input hamesha valid hoga.
    Udaharan:
    multiply(148, 412) ka return hoga 16.
    multiply(19, 28) ka return hoga 72.
    multiply(2020, 1851) ka return hoga 0.
    multiply(14,-15) ka return hoga 20.
    """
    result = a*b
    # looping through the given digits
    # if there are duplicate digits
    # we have failed!
    # We have reached the maximum nummber and we do the trick
    # with the first duplicate number
    counter = 0
    for i in range(a):
        if(counter > b):
            # if a is greater than b then we exit the while loop
            break   
        
        counter+=1
        if result < 0:
            result += b
    return result

print("The product of the numbers given is: ", multiply(19, 28))
print("The product of the numbers given is: ", multiply(148, 412))

print("The product of the numbers given is: ", multiply(19, 28))
print("The product of the numbers given is: ", multiply(2020, 1851))
