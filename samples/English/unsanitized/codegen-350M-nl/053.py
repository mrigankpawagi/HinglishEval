

def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    print "Add ", x, y, " to ", x+y, "."
    addx(x+y, x, y)

    yield x, y

add(1)
add(11)
add(30)
sub()

add(1)
add(2)
add(111)
sub()

print add(1, 6)

print add((1, 3), 6)

sub()
sub(10, 45)

# the program prints:
# Add 6, 3
# Add 5, 12
# Sub 4-7, 6
# Sub 6, 10
# Sub 11, 45
# Add 111
# Sub 30, 9
# Sub 123, 90

