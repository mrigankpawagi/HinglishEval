


def sum_squares(lst):
    """
    "
    Ye function ek integers ki list lega. List ke saare entries ke liye, function integer entry ko square karega agar uska index 3 ka 
    multiple hai aur cube karega agar uska index 4 ka multiple hai aur 3 ka multiple nahi hai. Function un entries ko change nahi 
    karega jinki indexes 3 ya 4 ka multiple nahi hai. Phir function saare entries ka sum return karega. 
    
    Examples:
    Agar lst = [1,2,3] hai to output 6 hona chahiye
    Agar lst = []  hai to output 0 hona chahiye
    Agar lst = [-1,-5,2,-1,-5]  hai to output -126 hona chahiye
    """
    n = len(lst)
    j = 0
    sum = 0
    if n > 0:
        for i in range(n):
            if i % 3 == 0:
                if i % 4 == 0:
                    j = lst[i] ** 3
                else:
                    j = lst[i] ** 2
            sum = sum + j
    return sum


# In[2]:


lst = [1]
sum_squares(lst)


# In[3]:


# Check if your output is correct above

assert sum_squares([]) == 0
assert sum_squares([1]) == 1
assert sum_squares([1, 2, 3]) == 6
assert sum_squares([-1, 2]) == -1
assert sum_squares([-1, -5, 2, -1, -5]) == -126


# Now we will test your function using several numbers of different values
# These are the expected output for each input
# Use those to test your solution
# (you should not print anything for this assignment)
print("Enter your answers as requested and write code to test your solutions ")
print("Note: If you have 64 entries in the inputs, write this number at the beginning of the line and the outputs with a space in-between each output")
print("Use the following syntax: 64 144 144 144 144")
print("Input:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
print("Output: 480")
print("Input:  [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]")
print("Output: -756")
print("Input:  [-1, -2, -1, -2, -1, -2, -1, -2, -1, -2]")
print("Output: -228")
print("Input:  [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]")
print("Output: