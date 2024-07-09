
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    if is_happy(s):
        return True
    elif not is_happy(s):
        return False
    return False
return is_happy(a) for b in s

A:

Here is one way
>>> for key, value in [
    key, key,
    key,
    key,
    key, key,
   ...
].items():

>>>    if key == key:
        return False
    elif '%s' in key:
        return True
else:
    raise ValueError("Unknown key %s" % (key,))

And there's no need to create a tuple
>>> '%s' in ('aa', 'b')
True

