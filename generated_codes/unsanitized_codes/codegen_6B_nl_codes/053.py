

def add(x: int, y: int):
    """
    Do numbers x aur y ko jodo
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    # You get the idea.
    return x + y


print("Hello I'm John. \nAnd my name is John. John is a great name. I'm a good name too.\n")
num = int(input("\nWhat would you like to add\: "))
print("\nThe total is {}.\n".format(add(num, num)))

A:

The error was in add, not in main.
You need to pass input arguments to add, like so: add(num, num)

As @DaiDai suggested in the comments, remove the global num, you never use it there but you used global in add!

Use print(f'...') for the prompts.
Use Python's print function instead of Python's standard output for your output. 
Don't use the hard coded string '\n'. It may break in the future, plus it's a pretty ugly hack.

The fix:
import math

