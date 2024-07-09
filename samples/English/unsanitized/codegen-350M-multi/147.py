
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    a = [i for i in range(n+1)]
    res = []
    
    for num in range(1, n+1):
        max_triple = 1
        for i in range(num):
            new_num = num + i
            for j in range(new_num):
                new_num = new_num - j
                d1 = i * i + i + j
                d2 = j * j + j + i
                x = 0
                while x < k:
                    y = i * i + j; x += k
                    if y in a:
                        x = x - k
                    z = new_num * new_num - x
                    z1 = z * z + z + 1
                    z2 = z1 * z1 + z2 + 1
                    if z2 == 0:
                        if z1 * z2 == 0:
                            z2 = z1
                        new_num += z
                    elif z2 == 0:
                        x -= k
                    t = d1 + z2 + d2
                    if t == num:
                        t = t - d2
                        max_triple = t
                        res.append(num)

        res.append(max_triple)
        
    res.sort()
    return res[-1]


if __name__ == '__main__':
    answer = get_max_triples(4)
    print("The last three terms are:",