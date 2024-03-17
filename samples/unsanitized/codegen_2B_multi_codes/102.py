def choose_num(x, y):
    """
    Yeh function do positive numbers x aur y leta hai aur return karta hai
    sabse bada even integer jo range [x, y] mein inclusive hai. Agar
    aisa koi number nahi hai, toh function ko -1 return karna chahiye.

    Jaise ki:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    return min(y, x) - 1


if __name__ == "__main__":

    x, y = 21, 17
    num_a = min(choose_num(x, y), y - 1)
    num_b = min(choose_num(x, y), y - 1)

    print(num_a + num_b)
