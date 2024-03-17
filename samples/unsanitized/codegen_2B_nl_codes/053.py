

def add(x: int, y: int):
    """
    Do numbers x aur y ko jodo
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x+y

A:

You could simply use the return statement for that. 
The advantage is, using the return in this way, you actually don't write all of those else statements. When there is no return for the last line, the function ends and there is no more if, else, while or for statements. When you write more than one return statement, you do use more if statements, but this is actually more readable.
For more details on the return statement, have a look here. 

