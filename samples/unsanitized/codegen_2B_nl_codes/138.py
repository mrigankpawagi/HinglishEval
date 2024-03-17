
def is_equal_to_sum_even(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 4 positive even numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n == 4:
        d = 1
    else:
        d = 1 if n % 2!= 0 else 2
    return (n <= d) & (n >= d+4)

print(is_equal_to_sum_even(5))

Solution
Your solution works on python but not on jupyter / ipython i guess. If you want to have it on python you need to do following:

Install Jupyter and install jupyter notebook
Jupyter provides a package named jupytext for converting plain text, latex, and code to be displayed in a notebook.
You can install jupytext package by using pip install jupytext
Run jupytext --help

Then you can modify your code to check if the sum of 4 consecutive non-negative even numbers, for example numbers 1 to 4, is equal to the sum of their squares, for example their squares should be 1, 4, 9 and 16. 
Your code now looks like this:
import math
import jupytext
from textwrap import dedent

