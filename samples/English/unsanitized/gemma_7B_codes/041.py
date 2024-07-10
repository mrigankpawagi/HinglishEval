

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

    cars_on_field = {i: "Y" for i in range(n, 0, -1)}
    left_to_right_cars = []
    left_to_right_cars.append(0)
    right_to_left_cars = []
    right_to_left_cars.append(n - 1)

    while True:

        # ek hi direction me bhari cars ko segregate karna
        cars = {
            "left_to_right": [],
            "right_to_left": [],
        }

        for i in left_to_right_cars:
            cars["left_to_right"].append(i - 1)

        for i in right_to_left_cars:
            cars["right_to_left"].append(i + 1)

        collision_happen = False

        # ek ek turn ke baad, ek baar agar koi gaadi takraati hain,
        # toh unka movement reverse hone laga hai
        for key, value in cars.items():
            if key == "left_to_right":
                tmp = [-1 for i in value]
                tmp[0], tmp[len(value) - 1] = value[len(value) - 1], value[0]

            else:
                tmp = [1 for i in value]
                tmp[0], tmp[len(value) - 1] = value[0], value[len(value) - 1]

            for car in range(len(value)):
                if cars_on_field[tmp[car]] == "Y":
                    collision_happen = True
                    cars_on_field[value[car]] = "N"

            if collision_happen:
                left_to_right_cars = tmp["left_to_right"]
                right_to_left_cars = tmp["right_to_left"]
                break

        if not collision_happen:
            break

    return cars_on_field.count("Y")


if __name__ == "__main__":

    n = int(input())
    assert int(car_race_collision(n)) == int(input())
