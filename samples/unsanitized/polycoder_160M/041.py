

def car_race_collision(n: int):
    """
    Socho ek road ko jo ek perfectly straight aur infinitely long line hai.
    n cars left se right ki taraf ja rahi hain; saath hi, ek alag set of n cars
    right se left ki taraf ja rahi hain. Dono set of cars shuruat mein ek dusre se bahut door hoti hain.
    Saari cars same speed mein move karti hain. Do cars tab takraati hain jab
    ek car jo left se right ja rahi hoti hai, right se left ja rahi car se takraati hai.
    Lekin, cars infinitely sturdy aur strong hoti hain; isliye, unka movement
    unke trajectory mein continue hota hai jaise ki unka collision hua hi nahi.

    Ye function aise collisions ki sankhya output karta hai.
    """

    m = len(n)

    if m == 10:
        return [0]

    if m <= 6:
        haa = n - 1
    else:
        haa = (n - 1) - 3

    karc = m - 3

    if karc > 10:
        karc = 10

    if karc < 5:
        karc = 5

    s = np.sqrt(n - m)
    res = np.sum(karc * s, axis=1)
    return haa * res

