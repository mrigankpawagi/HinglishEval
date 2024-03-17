

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
    # Write your code here
    # n cars left se right ki taraf ja rahi hain; saath hi, ek alag set of n cars
    # right se left ki taraf ja rahi hain. Dono set of cars shuruat mein ek dusre se bahut door hoti hain.
    # Saari cars same speed mein move karti hain. Do cars tab takraati hain jab
    # ek car jo left se right ja rahi hoti hai, right se left ja rahi car se takraati hai.
    # Lekin, cars infinitely sturdy aur strong hoti hain; isliye, unka movement
    # unke trajectory mein continue hota hai jaise ki unka collision hua hi nahi.
    #
    # Ye function aise collisions ki sankhya output karta hai.
    #
    # Input Format
    # A single integer n.
    #
    # Constraints
    # 1 <= n <= 1000
    #
    # Output Format
    # A single integer.
    #
    # Sample Input
    # 3
    # Sample Output
    # 1
    # 2
    # 3
    # Explanation
    # 1st car left se right ja rahi hai, right se left ja rahi car takraati hai.
    # 2nd car left se right ja rahi hai, right se left ja rahi car takraati hai.
    # 3rd car left se right ja rahi hai, right se left ja rahi car takraati hai.
    #
    # 1st car left se right ja rahi hai, right se left ja rahi car takraati hai.
    # 2nd car left se right ja rahi hai, right se left ja rahi car takraati hai.
    # 3rd car left se right ja rahi hai, right se left ja rahi car takraati hai.
    #
    # 1st car left se right ja rahi hai, right se left ja rahi car takraati hai.
    # 2nd car left se right ja rahi hai, right se left ja rahi car takraati hai.
    # 3rd car left se right ja rahi hai, right se left ja rahi car takra
