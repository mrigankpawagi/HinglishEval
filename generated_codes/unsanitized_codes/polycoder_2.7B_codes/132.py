
def is_nested(string):
    """
    Ek function banao jo sirf square brackets wala string input ke roop mein leta hai.
    Function tabhi True return karega jab valid subsequence of brackets ho 
    jisme kam se kam ek bracket nested ho.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    """
    if string == "[]"]:
        return False
    arr = ""
    for char in string:
        if char == ">":
            for char in string:
                if char == "]":
                    return True

        if arr!= "":
            if (char == ">") or (char == "]") or (char == "") or (char == "]") or ((char == "]") and (arr[0] == "[")):
                return False
            arr += char
    return False
