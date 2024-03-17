
def by_length(arr):
    """
    Ek array diya gaya hai integers ka, integers ko sort karo jo 1 se 9 ke beech mein hai,
    resulting array ko reverse karo, aur phir har digit ko uske corresponding name se replace karo 
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    Jaise ki:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> arr ko sort karo -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> arr ko reverse karo -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      Agar array khali hai, toh ek khali array return karo:
      arr = []
      return []
    
      Agar array mein koi ajeeb number hai toh use ignore karo:
      arr = [1, -1 , 55] 
            -> arr ko sort karo -> [-1, 1, 55]
            -> arr ko reverse karo -> [55, 1, -1]
      return = ['One']
    """
    if len(arr) == 0:
        return []
    arr.sort()
    arr.reverse()
    result = []
    for i in arr:
        if i >= 1 and i <= 9:
            if i == 1:
                result.append("One")
            elif i == 2:
                result.append("Two")
            elif i == 3:
                result.append("Three")
            elif i == 4:
                result.append("Four")
            elif i == 5:
                result.append("Five")
            elif i == 6:
                result.append("Six")
            elif i == 7:
                result.append("Seven")
            elif i == 8:
                result.append("Eight")
            elif i == 9:
                result.append("Nine")
    return result
