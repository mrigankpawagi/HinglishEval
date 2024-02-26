
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
    number = int(a)
    product = 0
    while number > 0:
        if number%10 == 0:
            product *= 10
        else:
            product = product + number%10
        number/=10
    return product

print("Enter the first number: ")
number = int(input())
print("Enter the second number: ")
second = int(input())
print("The product is: %s" % multiply(number,second))
print("Enter again: ")
second = input()
print("The product is: %s" % multiply(number,second))

Enter the first number:
8
Enter the second number:
12
The product is: 16
Enter again:

Enter the first number:
20
Enter the second number:
10
The product is: 0.008
Enter again:

Enter the first number:
-15
Enter the second number:
20
The product is: 20
Enter again:

Thanks!

A:

You need change the product in place.
You need to remember what's been processed and do the calculation by only one iteration. That is, remember what's the value of the processed number and how many it's been multiplied. If the current number is 10, then multiply all the result but the "current product" and add 1 to the product's counter. Do it in an loop until the current product equals the desired result.
I don't know Java, so I'm providing pseudo-code and