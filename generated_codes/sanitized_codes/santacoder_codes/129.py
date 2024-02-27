def minPath(grid, k):
    """
    Ek grid di gayi hai N rows aur N columns ke saath (N >= 2) aur ek positive integer k,
    grid ke har cell me ek value hai. Har integer range [1, N * N]
    inclusive grid ke cells par exactly ek baar appear hota hai.

    Aapko grid me length k ki minimum path find karni hai. Aap kisi bhi cell se start
    kar sakte ho, aur har step me aap kisi bhi neighbor cell me move kar sakte ho,
    dusre shabdo me, aap un cells me ja sakte ho jo aapke current
    cell se edge share karte hain.
    Dhyan dijiye ki length k ki path ka matlab hai exactly k cells visit karna (not
    necessarily distinct).
    Aap grid ke bahar nahi ja sakte.
    Ek path A (length k ki) ko path B (length k ki) se kam maana jata hai agar
    cells par jin values ko A aur B go through karte hain unki ordered lists banane ke baad (unhe hum lst_A aur lst_B kehte hain), lst_A lst_B se lexicographically kam hota hai, dusre shabdo me, ek integer index i exist karta hai (1 <= i <= k)
    jahan lst_A[i] < lst_B[i] aur kisi bhi j (1 <= j < i) ke liye hum
    lst_A[j] = lst_B[j] rakhte hain.
    Yeh guarantee ki gayi hai ki answer unique hoga.
    Return karo ek ordered list of the values jin cells se minimum path go through karti hai.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
