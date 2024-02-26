
def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.

    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    l = len(lst)
    if l < 2:
        return []
    try:
        even = [int(i) for i in lst]
        odds = [int(i) for i in lst[1:l//2] + lst[l//2+1:l]]
        even.extend(odds)
        even.sort()
        return even
    except Exception as e:
        print('Exception occured:\n{0}'.format(e))
        return []

print(add([100, 5, 2, 3, 4, 7]))

