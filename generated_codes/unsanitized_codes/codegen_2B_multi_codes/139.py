
def special_factorial(n):
    """
    Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! *... * 1!
    jaha n > 0

    Jaise ki:
    >>> special_factorial(4)
    288

    Ye function ek integer input ke roop me lega aur is integer ka special
    factorial return karega.
    """
    return int(round(expm1(-1.0 * n ** (1.0 / 2.0)) * jahaki_factorial(n - 1)))


class Functor(object):
    name = "Functor"
    short_name = ""

    def __init__(self, doc=None):

        self.functor()

    def setup_special_factorials(self, func=special_factorial):

        self.n = 0

        for i in range(1, 10000):
            self.n += 1
            self.facs_list.append(func(i))

    def print_functor(self, arg=[]):

        sorted_facslist = sorted(self.facs_list, key=lambda x: x, reverse=True)

        for j, fac in enumerate(sorted_facslist):
            print "{0}({1})".format(self.name, j)
            print arg + [fac]


class Calculation(object):
    functors_list = []

    def setup(self, doc=None):

        pass

    def get_functor(self, n):
        for i in range(len(self.functors_list)):
            if n == self.functors_list[i].facs_list[0]:
                return self.functors_list[i]
        return None

    def update_functors_list(self, n, facs_list):
        for i in range(len(self.functors_list)):
            if n == self.functors_list[i].facs_list[0]:
                self.functors_list[i].update_facs_list(facs_list