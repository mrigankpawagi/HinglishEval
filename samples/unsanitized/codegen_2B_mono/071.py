
def triangle_area(a, b, c):
    """
    Trikon ke teeno sides ke lengths diye gaye hain. Agar teeno sides ek valid trikon banate hain to trikon ka area 2 decimal points tak round off karke return karo.
    Anyatha -1 return karo.
    Teen sides tabhi ek valid trikon banati hain jab kisi bhi do sides ka yog teesri side se adhik hota hai.
    Udaharan:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    """

    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    return (a + b + c) / 2


print(triangle_area(3, 5, 10))   #6.0
print(triangle_area(18, 5.5, 2)) #-1
print(triangle_area(1, 1, 1))    #0.0

#################################################
"""
Exercise 2) Find the minimum number of platforms needed at that the cows and bulls would be able to play in a given n*m grid.

Function Description
Complete the function minimumNumberPlatforms in the editor below.

minimumNumberPlatforms has the following parameter(s):
- n, an integer representing the number of rows
- m, an integer representing the number of columns
- firstCowsMilk, a string of length m that represents the number of cows that have been milked in the format {x1}{x2}{…}{xm} where xi is either 'c' or 'b'
- firstCowsBulls, a string of length m that represents the number of cows that have been initially buffered at that column

Returns:
- Int, representing the minimum number of platforms needed to play the game

Example 1
Input
(3, 4, "1bc1c2b3b4c3b4b",  "cbcbaccc")
Output
3
Explanation
The cow grid looks as follows:

c b c
b c c
1 c