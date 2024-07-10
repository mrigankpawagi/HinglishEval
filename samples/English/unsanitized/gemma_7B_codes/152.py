
def compare(game,guess):
    """
    Mujhe lagta hai hum sabko woh ehsaas yaad hoga jab kisi besabri se intezaar karne wale event ka result finally pata chalta hai. Us samay jo aapke feelings aur vichar hote hain, unhe note down karna aur compare karna zaroori hota hai.
    Aapka task hai yeh determine karna ki kya ek vyakti ne kisi matches ke results ko sahi tara se guess kiya hai ya nahi.
    Aapko do arrays diye jayenge scores aur guesses ke, jinka length equal hoga, jahan har index ek match ko dikhata hai. 
    Wapas ek array return karo jiska length same ho, jo denote karta hai ki har guess kitna off tha. Agar unhone sahi guess kiya hai,
    toh value 0 hogi, aur agar nahi, toh value guess aur score ke beech ka absolute difference hoga.
    
    
    Udaharan:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    result=[abs(guess[i]-game[i]) for i in range (0,len(game))]
    return result

# Question 2

def all_prime_factors(number):
    '''
    Itne dinon se humari zindagi ne isse ghussa liya hai. Kabhi gharwala, kabhi bimawala aur kabhi loan-wala.
    Main bolu yaha kuch aur bhi baatein hai, agar pata chal jaaye toh kaafi pressure ho jata hai.
    Iss ke beech humko apne pocket mein jaadiya rakhna hai, or apna loan amount adjust karna hai.
    Main bhi kisi aur ka loan lagai hai, or usko bhi koi loan lagai hai, sab pe sab loan cycle chal raha hai.
    Par jab main ek hi phone pe koi aur bhi app launch karau, toh main apne paiso ko adjust nahi kar paata.
    Main usse ek alag jhaaz pe lagana chahta hu jisse main paisa adjust kar chuka hoon, or usske niche kuch aur bhi app launches kar pau.
    

    Udaharan -

    all_prime_factors(16) -> [2,2,2,2]
    all_prime_factors(100) -> [2,2,5,5]
    all_prime_factors(217) -> [11,19]
    all_prime_factors(4513247) -> [53, 53,53,53, 53]
    
    
    '''
    if number%2==0:
        return [2]+all_prime_factors(number//2)
    counter=1
    while (number%counter==0):
        counter+=1
    
    return [counter]+all_prime_factors(number//counter)


# Question 3

def make_key(string, key):
    '''
    Hume pta hai ki kahi pe ye bhi nahi pata chalta ki hum key ka use kaise kar rahe hain.
    Main toh unhe ek alag kaam dikha diya aur woh bhi aur sahi tarah se kar rahe tha.
    Main woh bhi karke dikha diya ki main hum