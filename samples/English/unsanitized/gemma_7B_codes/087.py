
def get_row(lst, x):
    """
    Aapko ek 2 dimensional data diya gaya hai, ek nested lists ke roop mein,
    jo matrix ke saman hai, lekin, matrices ke unlike,
    har row mein alag number of columns ho sakte hain.
    Diye gaye lst, aur integer x, list mein integers x ko dhundho,
    aur tuples ki list return karo, [(x1, y1), (x2, y2) ...] aisa ki
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
    # YOUR CODE HERE
    
    # 4
    # 4
    # [[1,2,3], [2,3,4], [1,3,2]]
    
    # [[1,2], [3,4]]
    
    lst2 = []
    
    for i in lst:
      idx = i.index(x)
      lst2.append((i.index(x),i.index(x)))
    
    lst2.sort()
    return lst2

def find_squares(lst):
  """
  Aapko list hi list ka ek array diya gaya hai,
  jaisa ke [32, 65, 44, -213, 1, 0, -2, -3, 1, 2, 3],
  kafi random hone ka.
  Sab integers hai, baaki jaata jae.
  Saath hi, -100 to 100 ke beech me.
  Aapko squares ke integers ke sarak (arrays) ko aapko 100 integers mehanga ke,
  har row me 10 integers ke,
  har list ke, pehle integers, sort karke.
  Baaki ki space nulls se fill karo.
  """
  
  # YOUR CODE HERE
  
  lst2 = []
  
  for i in range(100):
      lst2.append([])
      
  for i in lst:
    if -100 <= i <= 100:
      if i < 0:
        i *= -1
      
      lst2[i//10].append(i)

  for i in range(100):
    for j in lst2[i]:
      pass
  	if j == 0:
  	  lst2.append(j)
    else:
  	  lst2[i] = sorted(lst2[i])
  
  return lst2


def find_duplicates(lst):
  """
  Aapko sorted list diya gaya hai,
  kafi random hone ka, but integers ke sarak hai, jaisa ke [30, 31, 40, 41