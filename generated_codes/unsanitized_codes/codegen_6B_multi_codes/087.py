
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
    for m in xrange(0, len(lst)):
        if x == lst[m]:
            return m, 0
    return None, None

