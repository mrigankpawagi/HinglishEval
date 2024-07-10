
def make_a_pile(n):
    """
    Ek positive integer n diya gaya hai, aapko n levels ki ek pile of stones banani hai.
    Pehle level me n stones honge.
    Agla level stones ka number hoga:
        - agla odd number agar n odd hai.
        - agla even number agar n even hai.
    Har level me stones ki sankhya ko ek list me return karo, jaha index
    i ki element level (i+1) me stones ki sankhya ko darshata hai.

    Udaharan:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    if n == 1:
        return [1]
    elif n == 2:
        return [2,4]
    output = make_a_pile(n-1)
    # output.append(n-1)
    # if output[-1] == n:
    #     if n % 2 == 0:
    #         output.append(n + 1)
    #     else:
    #         output.append(n + 2)
    # else:
    if n % 2 == 0:
        output.append(n+1)
    else:
        output.append(n+2)
    return output


######################################################################
# This part just prints your result to our test runner to verify
# you did the right thing.
#
# DO NOT MODIFY!
#
def answer(expected,result):
    if expected == result:
        try:
            print "Case #%d: Yay! Answer is %s." % (test,result)
        except NameError, e:
            print "Case #%d: Yay! Answer is %s." % (id,result)
        
    else:
        try:
            print "Case #%d: Bummer! We expected %s but got %s." % (test,expected,result)
        except NameError, e:
            print "Case #%d: Bummer! We expected %s but got %s." % (id,expected,result)
        
def test_case(expected,function):
    global test
    global id
    test = 1
    id = 1
    answer(expected,function.result)
    
def run_tests():
        
    global id
    id = 2
    
    def _func():
        return make_a_pile(3)
    
    answer( [3, 5, 7], _func)

    global test
    test = 3
    
    def _func():
        return make_a_pile(0)
    
    answer([1],_func)

    global test
    test = 4
    global id
    id = 4
    
    def _func():
        return make_a_pile