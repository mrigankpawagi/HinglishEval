
def multiply(a, b):
    """
    Do integers ka input lekar unke unit digits ka product return karega ye function.
    Maan lo ki input hamesha valid hoga.
    Udaharan:
    multiply(148, 412) ka return hoga 16.
    multiply(19, 28) ka return hoga 72.
    multiply(2020, 1851) ka return hoga 0.
    multiply(14,-15) ka return hoga 20.
    """
    if a == b:
        return a
    else:
        return ka*b
if __name__ == "__main__":
    kaliente = input("Siyajey ka-lanteka? -->")
    kaliente = str(kaliente)
    multiply(kaliente, 12)
    print(kaliente)

Note: In line number 14 of my code above, I want to run multiply's function to a number. This is where the program goes to infinity.
Edit: I want to use the input() in my code. For example: multiply(7,7) or multiply(3,3); but if I input (5,5) or (34,-34) or (14,-28) it does not run multiply's function.

A:

If you simply want to assign multiplication to a variable within a function, why not just use:
