from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Diye gaye numbers ki list (kam se kam do elements ki) par ek linear transform apply karo,
    aisa ki sabse chota number 0 ban jaye aur sabse bada number 1 ban jaye
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    kam, elements = numbers
    res_k1, res_k2, res_k3 = [], [], []
    for i, (k, s, _) in enumerate(elements):
        cur_k = kam
        cur_s = k
        try:
            cur_s, cur_k = s[k], cur_s
        except:
            cur_s, cur_k = s[-1], s[0]
        k = s[i]
        for j in range(npt - 1):
            cur_k = np.clip(cur_k, 0.0, npt - k1 - 1)
        res_k1.append(res_k1[-k1])
        res_k2.append(
            res_k2[-k2 - 1] + np.sqrt(np.square(res_k1)) if k2 - 1 >= 0 else 1
        )
        if k1[0] < cur_k[0]:  # pis auras
            for i in range