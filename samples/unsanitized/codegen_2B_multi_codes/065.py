
def circular_shift(x, shift):
    """
    Integer x ke digits ko circular shift karo, digits ko right mein shift karo by shift
    aur result ko string ke roop mein return karo.
    Agar shift > digits ki number ho, toh reversed digits return karo.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    #if shift <= len(str(x)):
    #    return x
    return str(x)[-shift-1::] + str(x)[:-shift:]
#    if shift <= len(str(x)):
#        return x
#    shifted_s = x[-shift:] + x[:-shift]
#    for i in range(len(shifted_s)):
#        if shifted_s[i] >= '9':
#            shifted_s = shifted_s[:i] + shifted_s[i+1:]
#            break
#    while shifted_s[-1] > '9':
#            shifted_s = shifted_s[:-1]
#    if shifted_s[-1] == '9':
#        shifted_s = shifted_s[:-1] + '0'
#    #    print shifted_s
#    return shifted_s

x = 20
shift = 2
shifted_s = circular_shift(x, shift)
#for i in range(len(shifted_s)):
#    if shifted_s[i] >= '9':
#        shifted_s = shifted_s[:i] + shifted_s[i+1:]
#        break
while shifted_s[-1] >= '9':
    shifted_s = shifted_s[:-1]
    shifted_s = shifted_s[:-1] + '0'

#    print shifted_s
print shifted_s
