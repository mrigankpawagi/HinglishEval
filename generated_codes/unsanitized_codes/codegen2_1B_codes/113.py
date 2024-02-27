
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
    karnoi=list(map(int,lst))
    odd_number=0
    for i in filter(lambda x: not((x%2==0)&(odd_number < len(karnoi)-1)),karnoi):odd_number=odd_number+1
    return list(karnoi)+[f"input ki {odd_number} mein odd elements ki sankhya"]
