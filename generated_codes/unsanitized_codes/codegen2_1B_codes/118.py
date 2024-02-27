
def get_closest_vowel(word):
    """
    Aapko ek word diya gaya hai. Aapka task hai right side se dekhte hue us vowel ko dhundna hai jo 
    do consonants ke beech mein hai (case sensitive).
    
    Shuruat aur ending mein jo vowels hain unka count nahi hoga. Agar aapko koi bhi vowel upar diye gaye 
    condition ke hisaab se nahi mila toh khali string return karo. 

    Aap maan sakte ho ki diya gaya string sirf English letters se bana hua hai.

    Udaharan:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    m_i = numpy.zeros(len(word))
    m_j = [None]*(len(word)+1)
    
    i=0;j=1;
    while(i==0 or j==0):
    <mask_1>_ij,n_i = numpy.inf,numpy.inf
    i_end,j_end,i_start,j_start = None,None,0,0
    
    while n_i < numpy.abs(m_i).sum():
    #