
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
    
    result = []
    if isinstance(lst, str):
        if len(lst)!= 3:
            lst = [str(element) for element in lst]
            result.append(f"input ki string {lst}")
        else:    
            for i in range (0, len(lst)//2):
                n = lst[i]
                if n[0] in string.digits and n[1]!= "9":
                    result.append(f"{n[0]} {n[1]}")
                    return result 
    else:
        return lst
    return result   


result = odd_count(['1234567'])
print(result)

result = odd_count(['3',"11111111"])
print(result)
print(type(result), type(string.digits))

result = odd_count(['3',"11111111"])
print(result)
print(type(result), type(string.digits))
