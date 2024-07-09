

def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    def get_dist(car1, car2):
        return abs(car1[1]-car2[1])

    def get_collision_distance(car1, car2):
        return max(carsize, get_dist(car1, car2))

    def process_movement(car1, car2):
        if not (car1[0] or car2[0] ): return 0

        if car1[0] > car2[0] :
            if car1[1] > car2[1]: car1[1] = car2[1]
            if car1[1] < car2[1]: car1[1] = -car2[1]
        else:
            if car1[1] > car2[1]: car2[1] = -car1[1]
            if car1[1] < car2[1]: car2[1] = car1[1]

        return (car1[0] + car2[0]) * get_collision_distance(car1, car2)

    def collision_