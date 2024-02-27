def tri(n):
    """
        Sabhi ko Fibonacci sequence ke baare mein pata hai, yeh mathematicians
    ne pichle kuch sadiyon mein gahrai se adhyayan kiya. Lekin, jo log nahi jaante
    woh hai Tribonacci sequence.
        Tribonacci sequence ko define kiya gaya hai recurrence ke dwara:
        tri(1) = 3
        tri(n) = 1 + n / 2, agar n even hai.
        tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), agar n odd hai.
        Jaise ki:
        tri(2) = 1 + (2 / 2) = 2
        tri(4) = 3
        tri(3) = tri(2) + tri(1) + tri(4)
               = 2 + 3 + 3 = 8
        Aapko ek non-negative integer number n diya jayega, aapko Tribonacci sequence ke pehle n + 1 numbers ka ek list return karna hai.
        Examples:
        tri(3) = [1, 3, 2, 8]
    """
    k = map(int, self.split("."))
    if not k == n:
        raise ValueError(
            f"Triine sequence expected, pedagopalo dekanne kelkia kayas hai seadhyayane ko hai se eni teoracci jika ke mein patahai."
        )
    ka = [(1, n)] * 6  # kayan patahai.
    k_max = [map(int, ka) for ka in k]
    l = []
    for i in range(0, n):
        m = k[(3 * i) + 1]
        l
