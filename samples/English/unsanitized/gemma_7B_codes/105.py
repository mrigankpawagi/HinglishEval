
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
        
    dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    output = []
    temp = []
    for i in range(1,10):
        temp.append(dict[str(i)])
    if(len(arr) == 0):
        return []
    else:
        arr.sort()
        arr.reverse()
        ind = len(arr) - 1
        for i in range(len(arr)) :
            if(arr[i] in temp):
                output.append(str(i + 1))
            else:
                output.append('One')
        return output   
#     if(len(arr) == 0):
#         return []
#     else:
#         #temp = set()
#         #temp = [set() for _ in range (9)]
#         for i in range(len(arr)):
#             print(i)
#             if(arr[i] > 0):
#                 if(arr[i] in temp):
#                     print("i in temp")
#                     temp.pop(arr[i] - 1)
#                     temp.insert(0,arr[i])
#                     print(temp)
#             
#             else:
#                 try:   
#                     temp = set(temp)
#                     temp.remove(0)
#                 except:
#                     pass
#             print(temp) 
#            


# if __name__ == '__main__':
#     arr = [13 , -1 , -25, 20, 7, -3 ,55]
#     print(by_length(arr))
