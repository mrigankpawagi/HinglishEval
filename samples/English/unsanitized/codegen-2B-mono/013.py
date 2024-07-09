

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while a % b!= 0:
        a, b = b, a % b
    return b

#--------------------------------------------------------------------------------------------------------------

# Question 1 : Write a function whose input is a dictionary
# where each key is a string and each value is either an integer or a list or a dictionary.
# The function should return a list of the values that are dictionaries.
#
# Hint: Don't return any key from the input dictionary that is not a string or a list or a dictionary.
#
# An example input would be :
#      {
#         "a":"10",
#         "A":"20",
#         "b":"40",
#         "c":[50,60,70],
#         "g":"3.14159",
#         "h": {
#              "A":"2.71828",
#              "sadfsadf": "dfsdfsdf",
#              "123":2,
#              "2.2a2":{1,2,3},
#              "g": "asd"
#         },
#      }
#
# Answer : ['40','90','3.14159','120','2.7245','3.141592']
#


