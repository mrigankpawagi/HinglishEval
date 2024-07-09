
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    for i in range(num):
        num -= i
    return [i]


class Integer(object):
    def __init__(self, digits):
        self__digits = digits
        num = int(digits)

  def __repr__(self):
    return '%s (digits = %d)' % (str(self), num)


