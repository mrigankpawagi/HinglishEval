def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.
    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    print(lst)
    num = int(input("Enter number:\t"))
    if num < 2 or num > 29:
        print("Please enter an integer between 2 and 29.")
        add(lst)
    else:
        lst.append(num)
        print(add(lst))