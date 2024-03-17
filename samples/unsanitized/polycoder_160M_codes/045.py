

def triangle_area(a, h):
    """
    Ek side ki length aur height di gayi ho to, triangle ka area return karo.
    >>> triangle_area(5, 3)
    7.5
    """
    if a == 0.0:
        return 0

    n1, n2, n3, p = np.mod(np.linalg.norm(a - a, axis=1), 2 * np.pi), -np.ones(3)
    tmp1 = (a - a[2 * 3 + n1 - 1], a[-3 * 3 + n1 + 1]) + (a - a[2 * 3 +!n1], -3 * np.pi)
    tmp2 = a[3 * 2 - n1]
    tmp3 = a[2 * 3 +!n1]
    #tmp3 = a[0, 2 *!n1]
    tmp4 = -a[1 - n2]
    tmp5 = -(tmp2 - tmp3) * 1 / tmp3
    tmp6 = -(a[2 * 3 +!n1] + (a[2 * 3 +!n2] - a[2 * 3 - 1])) * 1 / tmp6
    tmp7 = (a[1 - n1] + 1) * tmp2 * tmp6
    #tmp7 = ((a[3 * 2 - n1] + 1 - a[3 * 2 +!n1]) + (a[2 * 3 +!n2] - a[3 * 2 -!n1])) * 4 / tmp7
    tmp8 = (a[1 - n1] - a[2 * 3 - 1]) * 1 / tmp7
    # tmp8 = -(a[1 - 1 - n1] + ((a[1 - 2 +!n1] + a[1 - n2]) * 2 / tmp7)) * 1 / tmp8
    # tmp10 = tmp8 - tmp15 / 8
    tmp11 = -(a[1 - 2 -!n1] +