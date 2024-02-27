
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
    if n == 1:
        return []
    elif n == 2:
        return [1, 3]
    else:
        final_list = [1, 3, 2, 8]
        for i in range(n - 3):
            final_list.append(sum(final_list[-3:]))
    print("Solve the question...")
    return final_list

# Question 5: Write a binary search function which takes a sorted arr a list and its target. The function returns if target
# is present into the list or not, it also returns the starting and ending index. If value is not found than return
# -1, -1
# Examples:
# Input: arr = [5,1,2,6], target = 3      Output: ([2,1,3], 0, 1)
# Input: arr = [4,1,2], target = 4          Output:([-1, -1], -1, -1)
# Input: arr