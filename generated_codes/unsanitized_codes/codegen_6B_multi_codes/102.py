
def choose_num(x, y):
    """
    Yeh function do positive numbers x aur y leta hai aur return karta hai
    sabse bada even integer jo range [x, y] mein inclusive hai. Agar 
    aisa koi number nahi hai, toh function ko -1 return karna chahiye.

    Jaise ki:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    # Check if x < y
    if x > y:
        raise ValueError("x should be lesser than y")

    # Check for odd num
    if (x % 2)!= (y % 2):
        return -1

    # If num is even
    if x!= y:
        return x - (x // 2)

    # Check for infinite loop
    for i in range(x, y + 1, 2):
        if (i < 0):
            raise ValueError("Cant choose num less than 0")
    print(x, y)

    result = x - (x // 2 + 1)
    return result

