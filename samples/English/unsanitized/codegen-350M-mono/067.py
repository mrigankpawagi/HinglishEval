
def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    fruit_apple = s.count('1')
    fruit_orange = s.count('3')
    n2 = fruit_orange + fruit_apple
    if n2 > n:
        res = n2
    elif n2 == n:
        if fruit_apple == fruit_orange:
            res = 8
        elif fruit_apple == 0:
            res = 2
        else:
            res = 2 + fruit_apple
    else:
        res = fruit_apple // n2
    return res

if __name__ == "__main__":
    """
    Here are some test cases...
    These are some 3-digit numbers that can be represented with one digit on each line:
    12 345
    12345
    123456
    """
    print(fruit_distribution("12 345",15 ))
    print(fruit_distribution("12345",15 ))
    print(fruit_distribution("123456",15 ))
    print(fruit_distribution("2",3))
    print(fruit_distribution("3",3))
    print(fruit_distribution("100",3))
    print(fruit_distribution("0",3))
    print(fruit_distribution("95",10))