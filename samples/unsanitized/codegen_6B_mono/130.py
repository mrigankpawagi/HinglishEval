
def tri(n):
    """
    Sabhi ko Fibonacci sequence ke baare mein pata hai, yeh mathematicians
ne pichle kuch sadiyon mein gahrai se adhyayan kiya. Lekin, jo log nahi jaante
woh hai Tribonacci sequence.
    Tribonacci sequence ko define kiya gaya hai recurrence ke dwara:
    tri(1) = 3
    tri(n) = 1 + n / 2, agar n even hai.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), agar n odd hai.
    Jaise ki:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    Aapko ek non-negative integer number n diya jayega, aapko Tribonacci sequence ke pehle n + 1 numbers ka ek list return karna hai.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """

    if n <= 0:
        print("Non-negative integers only")
        return None

    if n == 1:
        print ("For n = 1, returns [1].")
        return [1]

    elif n == 2:
        print ("For n = 2, returns [1, 3].")
        return [1, 3]

    else:
        return trib(n)


print (tri(3))
    



#--------------------------------------------------------------------------------------------#

"""
Question 17:
The Fibonacci sequence is defined recursively:
    F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1.
    
    Hence the first 12 terms will be: f0 = 0, f1 = 1, f2 = 1, f_n = 
    f_{n-1} + f_{n-2} for n > 2.

In the following Python program,