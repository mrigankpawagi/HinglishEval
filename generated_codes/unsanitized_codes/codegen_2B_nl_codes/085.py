
def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.

    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    m = len(lst)
    if m >= 0:
        return add(lst[::2]) + add(lst[1::2])
    else:
        return add(lst)



###############################################################################
#                                      Test Case                                   #
###############################################################################

if __name__ == "__main__":

    import getopt
    opts, args = getopt.getopt(sys.argv[1:], "ht:", [])
    h = 0
    t = 0

    for o, a in opts:
        if o == '-h': h += 1
        if o == '-t': t += 1

    if h!= 0:
        print('-h means horizontal view')

    if t!= 0:
        print('-t means vertical view')
    else:
        t = 0

    print(add(args[0], args[1:]))
