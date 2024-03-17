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
    arr = [str(i) for i in arr]
    return [str(i) for i in arr]
