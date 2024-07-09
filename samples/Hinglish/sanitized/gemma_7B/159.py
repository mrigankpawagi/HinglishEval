
def eat(number, need, remaining):
    """
    Tum ek bhukha khargosh ho, aur tumne pehle hi kuch gajar kha liye hain,
    lekin ab tumhe din bhar ke bhojan ko pura karne ke liye aur gajar khane ki zarurat hai.
    tumhe ek array return karna chahiye jisme [ tumhare bhojan ke baad khaye gaye total gajar,
                                    bhojan ke baad bache hue gajar ] ho.
    Agar bache hue gajar kafi na ho, to tum saare bache hue gajar kha loge, lekin phir bhi bhukha rahoge.
    
    Udaharan:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer
        gajar jo tumne pehle kha li hain.
    @need : integer
        gajar jo tumhe ab khane ki zarurat hai.
    @remaining : integer
        stock mein bache hue gajar ki sankhya
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Maza karo :)
    """
    return [number + need, remaining - need]
