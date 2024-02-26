
def odd_count(lst):
    """
    Ek strings ki list di gayi hai, jahan har string sirf digits se bani hoti hai, ek list return karo.
    Output ki har element i ko "input ki string i mein odd elements ki sankhya." ke roop mein hona chahiye, jahan saari i's ko input ki i'th string mein odd digits ki sankhya se replace kar dena chahiye.

    >>> odd_count(['1234567'])
    ["input ki string 4 mein odd elements ki sankhya 4."]
    >>> odd_count(['3',"11111111"])
    ["input ki string 1 mein odd elements ki sankhya 1.",
     "input ki string 8 mein odd elements ki sankhya 8."]
    """
    new_list = []
    for item in lst:
        new_string = ""
        for c in str(item):
            if int(c)%2!= 0:
                new_string = new_string + c
        new_list.append(new_string)
    return new_list

 #########################################


##############


    """
    Find the odd count in a list, and replace all the odd count in a string with "-".

    >>> str_with_odd_count("Hello")
    "Hello"
    >>> str_with_odd_count("Hello, my name is Harsha")
    "Hello-my name is-Harsha"
    >>> str_with_odd_count("Hello, my name is Harsha")
    "Hello-my name is------Harsha"
    """
import collections
