
def will_it_fly(q,w):
    """
    Ek function likho jo True return kare agar object q udega, aur False otherwise.
    Object q tabhi udega jab vo balanced ho (yani ki ek palindromic list ho) aur uske elements ka sum maximum possible weight w se kam ya barabar ho.

    Udaharan:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 maximum possible weight se kam hai, lekin ye balanced nahi hai.

    will_it_fly([3, 2, 3], 1) ➞ False
    # ye balanced hai, lekin 3+2+3 maximum possible weight se jyada hai.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 maximum possible weight se kam hai, aur ye balanced hai.

    will_it_fly([3], 5) ➞ True
    # 3 maximum possible weight se kam hai, aur ye balanced hai.
    """
<mask_1> (q,w))

    q = sorted([int(s) for s in q.split(",")])
    m = max(q)
    w = int(m/len(q) * len(q))

    res = False
    return res


if __name__=="__main__":
    q1 = ['2','13','21','12','42','13','21','33','13','21']
    q2 = ['2','13','23','13','42','14','32','13','23']
    q3 = ['13','42','21','34','12','22','12','42','32']
    q4 = ['2','13','21','34','13','42','13','42']

    """
    #