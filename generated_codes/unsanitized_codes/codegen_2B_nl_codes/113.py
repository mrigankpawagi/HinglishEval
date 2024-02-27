
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
    if not lst:
        return []
    else:
        temp = []
        first_odd = ""
        for i, x in enumerate(lst):
            if len(str(x)) % 2!= 0:
                s_num, d_num = str(x), int(str(x))
                odd_str = first_odd + str(s_num) + " " + str(d_num)
                first_odd = odd_str
                temp.append(odd_str)
        temp.append(first_odd)
        return temp

#
# Define the following variable as an integer
#
odd_input_length = 5
odd_strings = odd_count(odd_input_length)
print(odd_strings)

