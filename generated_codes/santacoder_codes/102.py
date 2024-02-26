
def choose_num(x, y):
    """
    Yeh function do positive numbers x aur y leta hai aur return karta hai
    sabse bada even integer jo range [x, y] mein inclusive hai. Agar 
    aisa koi number nahi hai, toh function ko -1 return karna chahiye.

    Jaise ki:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    print('hi')
    # 1st, 2nd, 3rd, 4th,...
    even_number = lambda x: x % 2 == 0
    # even
    if even_number(x) and even_number(y):
        return -1

    def f(a, b):
        # x < b, y < a
        if a <= b < x:
            return 1
        if a <= x < b <= y:
            return 2
        if a <= b <= x <= y:
            return 3
        if a > x:
            return 4
        if b > y:
            return 4
        return -1
    return f(x + y, y)

