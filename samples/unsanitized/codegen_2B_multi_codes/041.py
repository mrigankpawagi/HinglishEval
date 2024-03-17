

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
    # define a set of kartas
    cars = range(1, n+1)
    # define a set of kartas
    car_num = len(cars)

    # initialize variables
    # cars[i] is the position of car i
    # index in cars of car thats position i
    is_crashed = 0 #car crash status

    # list of indices of cars thats location
    car_located = [0] #car location - location i cars[i] are located on -
    # index car i, location i cars[i] where collisitons were detected
    index_collisions = 0
    index = 0 #location of car at index index_collisions

    # track the collisions
    collisions: typing.List[typing.Mapping[str, int]] = list()
    # initialise
    collisions = [[{} for x in range(car_num)] for x in range(car_num)]

    # index of location of collision
    for j in range(car_num):
        # index of location of car
        if j == car_num - 1: index = j
        for car in cars[j:]:
            while index < car:
                try:
                    # find car located