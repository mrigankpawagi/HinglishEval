
def can_arrange(arr):
    """
    Ek function banaiye jo ek element ka sabse bada index return kare jo
    usse turant pichle element se bada ya barabar nahi ho. Agar
    aisa koi element nahi hai, to -1 return kare. Diye gaye array me
    duplicate values nahi hogi.

    Udaharan:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    length = len(arr)
    result = 0
    for i in range(length):
        for j in range(i+1,length):
            if arr[i] == arr[j]:
                result += 1
    return result


if __name__ == "__main__":
    print can_arrange([1,2,4,3,5])