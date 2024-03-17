

def same_chars(s0: str, s1: str):
    """
    Dekho ki do shabd me same characters hai ya nahi.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    if len(s0)!= len(s1):
        return False

    chars = set(s1)
    if not os.path.exists(args.in_folder):
        os.system('touch %s' % (args.in_folder))
        return False

    s0_file = open(args.in_folder + '/%s.txt' % s0, 'w')
    s1_file = open(args.in_folder + '/%s.txt' % s1, 'w')
    s0_file.write(s0+'\n')
    s1_file.write(s1+'\n')

    def search(s, v, d, i=0):
        if d == s:
            s0_file.write(v + '\n')
            return
        if i >= 10:
            return
        search(s, v+'#', d, i+1)
        search(s, v+'%', d, i+1)
        search(s, '#', d, i+1)
        search(s, '%', d, i+1)

    search(s0, '%', (0-1), 0)
    search('', 'd', ((0-2)*1) + 1)  # zeros
    search('#', '#', ((0-2)*3) + 1)