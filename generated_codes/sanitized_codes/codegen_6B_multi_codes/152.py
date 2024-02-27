
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
    result = game
    for i,s in enumerate(guess):
        result[i] = max(int(guess[i]), int(game[i]))


    count = 0
    counter = 0
    #print result
    for item in result:
        counter+=result[item]
        if result[item]!=game[item]:
            count+=1

    return count, count*100.0/len(guess)
