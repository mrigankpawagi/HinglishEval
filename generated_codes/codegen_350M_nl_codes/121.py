
def solution(lst):
    """
    Ek non-empty list di gayi hai integers ki, return karo sum of all odd elements jo even positions pe hain.
    
    Udaharan
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    t1 = set()
    t2 = set()
    if len(lst) < 2:
        error('Please specify two even numbers')
    else:
        for i in xrange(len(lst)):
            if lst[i]!= '\'' and lst[i] ~= '[' or ']' or lst[i] ~= '=' or lst[i] ~= ',':
                raise ValueError('Ek non-empty elements')
            t1 += xrange(i-1)[0] + xrange(i-1)[1]
            t2 += xrange(i-1)[0] + xrange(i-1)[1]
    if t1 > t2:
        error('Ek non-empty elements')

tod = 0
cursor = 0
for i in xrange(len(lst)):
    try:
        while cursor < td and solution(lst[cursor]) == 'j:'.join(lst):
            cursor += 1
    except KeyError:
        cursor = 0
    for j in lst[cursor+1:] for j in [1, 2]:
        if solution(j) == 'j': c = 1
      