
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
    if isinstance(arr, (list, set, tuple)):
        arr = list(arr)

    def compare(arr1, arr2):
        flag = False

        if len(arr1) == len(arr2):
            for i in range(len(arr1)):
                if arr1[i] == arr2[i]:
                    flag = True
                    break

            return flag

        return False

    def replace(arr1, arr2):
        len_arr_2 = len(arr_2)
        str_tmp = ""
        if arr_2[:1] == "-":  # For - in reverse sort we need to consider 2 -, which is added in reverse order to end of the array
            len_arr_2 += 1
            str_tmp = arr_2[1:]
            arr_2 = arr_2[:1]

        for i in range(len(