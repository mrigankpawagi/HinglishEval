

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
    assert type(n) is int

    # code your solution here
    cars_map = [car() for i in range(n)]
    car_speed = speed()
    total_car_speed = 0

    for car in cars_map:
        car_speed = car.change_speed()

        for other_car in cars_map:
            if car_speed == other_car.speed:
                car.collision(other_car) # no need to check when we check car on map

    for car in cars_map:
        total_car_speed += car.speed
        car.x = car.change_coordinates(car.x[0], car.x[1], total_car_speed)

    return cars_map

