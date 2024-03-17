
def get_row(lst, x):
    """
    Aapko ek 2 dimensional data diya gaya hai, ek nested lists ke roop mein,
    jo matrix ke saman hai, lekin, matrices ke unlike,
    har row mein alag number of columns ho sakte hain.
    Diye gaye lst, aur integer x, list mein integers x ko dhundho,
    aur tuples ki list return karo, [(x1, y1), (x2, y2)...] aisa ki
    har tuple ek coordinate ho - (row, columns), shuru karte hue 0 se.
    Coordinates ko pehle rows ke hisaab se ascending order mein sort karo.
    Saath hi, row ke coordinates ko columns ke hisaab se descending order mein sort karo.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    x1, x2 = 0, []
    for i in range(len(lst)):
        if lst[i]!= '' and isinstance(lst[i], list):
            if i == 0:
                j = 0
            else:
                j = x2[len(x2) -1]
            m = [j, i]
            while m in x2:
                m = m[1:]
            x2.append(m)
            get_row(lst[x1:i], j)
            x1 = i
            j = 0
 
    if x1 < len(lst):
        return [(m[0], n-1) for m, n in zip(x2[:x1], (len(lst)-x1