
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
    if len(lst) == 0 or lst == []:
        return list(odd_count(['']))
    elif ''.join(lst) == '':
        return list(odd_count(*lst))
    elif ''.join(lst) in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return [''.join(lst)]
    else:
        return ['input ki string'+ str(frozenset(lst)) +'mein odd elements ki sankhya'+ str(sum(1 for x in lst if (x in (2, 6, 8, 9)) and x == int(x)))]


