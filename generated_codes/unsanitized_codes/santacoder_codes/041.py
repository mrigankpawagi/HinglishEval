

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
    if n == 0:
        return []

    def helper(lo: int, hi: int, k: Union[int, List[str]]) -> None:
        if lo == hi:
            return

        speed1 = get_speed(i1(lo, hi))
        speed2 = get_speed(i2(lo, hi))
        speed3 = get_speed(i4(lo, hi))

        if speed1!= '' and speed2!= '' and speed3!= '':
            speed1 = float(speed1.replace('kph', ''))
            speed2 = float(speed2.replace('kph', ''))
            speed3 = float(speed3.replace('kph', ''))

        if speed1!= '' and speed2!= '' and speed3!= '':
            max_dir = max(speed_dir(speed1), speed_dir(speed2), speed_dir(speed3))
            # print(max_dir)

        # If max_dir is null:
        if max_dir in ["L", "R"]:

            # If there is a corner case, we change max_dir to be either "L" or "R"
            # If neither of the points are within the boundaries, no edge must change.

            # A case with 2, 3, or 4 cars (as