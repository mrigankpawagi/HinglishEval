
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
    cnt = 0
    for s in lst:
        if s == "0":
            continue
        if s.isdigit():
            while s and s.isdigit() and cnt == 0:
                cnt = cnt + 1
        else:
            cnt = cnt + 1
    return str(cnt)

if __name__ == '__main__':
    inputList = [2, 4, 5, 6, 8, 10]
    result = odd_count(inputList)
    print("\n" + result + ".")
