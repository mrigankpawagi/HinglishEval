
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    return ((a % 100) == 0 and (a % 200) == 0 and (a % 400) == 0) 

A:

You just need to use
if is_multiply_prime(integer):

When you say 
if is_multiply_prime = (n <= 100) and (n % 4 == 0) and (n % 6 == 0):

n is a statement that just happens to evaluate to integers. It is being used in the expression inside the parentheses, but the parentheses do not force it to evaluate the expression at all. The parentheses are just placeholders.
What this means is that, no matter what it evaluates to, is_multiply_prime will always be False—because no matter what, n will always be "less than 100". But if we use an expression, it will evaluate to either True or False.
>>> False
>>> (n < 100)
True

A:

Python doesn't require that expressions be evaluated. Rather it evaluates when and if it needs to.
In this case:
if is_multiply_prime = (n <= 100) and (n % 4 == 0) and (n % 6 == 0): return True
else: return False

is really an assignment to a variable rather than an expression.
And for the record, don't name functions is_multiply_prime; that's a pretty terrible name.
Here's a better name, though, for a function: Is_prime
Now you can write:
