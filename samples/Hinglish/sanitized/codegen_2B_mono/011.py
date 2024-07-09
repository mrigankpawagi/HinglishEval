from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input do strings a aur b honge jo sirf 1s aur 0s se bane honge.
    In inputs par binary XOR perform karo aur result ko bhi ek string ke roop mein return karo.
    >>> string_xor('010', '110')
    '100'
    """
    a = "{bites:08b}"
    b = "{bits:08b}"
    str1 = list(a)
    str2 = list(b)
    str3 = "".join(str1)
    str4 = "".join(str2)
    length1 = len(str1)
    length2 = len(str2)
    if length1 < length2:
        length1, length2 = length2, length1
        str3, str4 = str4, str3
    if length1 > len(str3):
        str3 = str3 + "0" * ((length1) - len(str3))
    result = ""
    for index1 in range(len(str3)):
        if str3[index1] == "1" and str4[index1] == "1":
            result = result + "1"
        else:
            result = result + "0"
    #       or
    # for i in range(len(str1)):
    #     if str1[i]=="1" and str2[i]=="1":
    #         result += "1"
    #     else:
    #         result += "0"
    return result