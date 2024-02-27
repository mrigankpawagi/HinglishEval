
def encrypt(s):
    """
    Ek function banaiye encrypt jo ek string ko argument ke roop mein leta hai aur
    ek encrypted string return karta hai jisme alphabet ko rotate kiya gaya ho.
    Alphabet ko aise rotate karna chahiye ki letters 
    do se multiply kiye gaye do places ke neeche shift ho jaye.
    Jaise ki:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """

    #                                                                                     
    if s: #                                                                                             
        s = s.encode('UTF-8')                                                                                  
        s +=  u'$%(b' % bytes(int(time.time(), 4)), '0')
        s +=  u'$%(