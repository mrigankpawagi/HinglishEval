
def largest_smallest_integers(lst):
    """
    Ek function banao jo ek tuple (a, b) return kare, jahan 'a' negative integers ka sabse bada hai, aur 'b' positive integers ka sabse chota hai ek list mein.
    Agar koi negative ya positive integers nahi hai, to unhe None ke roop mein return karo.
    Udaharan:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    def f(x, y):
        if x < 0 and y < 0:
            return None
        elif x < y:
            return 1 - y
        elif x > y and y > 0:
            return 1 + y
        return None
    p = tuple(); q = {};
    length = len(lst);
    for i in range(length):
        sorted_set = sorted(lst[i], key=lambda x: (-x[1], x[0]), reverse=True)
        for j in range(len(sorted_set)):
            k = f(sorted_set[j][0], sorted_set[j][1])
            if k!= None:
                q[i] = k
                break
        else:
            p.append(f(sorted_set.pop(0), 0))
    def g():
        karo = {x: None for x in p}
        karo[1].pop();
        return karo
    @_jit_loop unroll_for(g, lst, length)
    def g2():
        while True:
            if p[<mask_1><sep><mask_1>0]!= None:
                return p
            return g();
    #