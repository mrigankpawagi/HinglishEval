

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
    # The main thing to do here is to get an accurate number of cars.
    numerator = abs(3) * (n + 2) + 10  * (n + 2) * (2 + 2)  + 6  * (n + 4)  * (2 * 2) + 6
    tot = (3 + 6) * (n + 2) + 10 + 18  * (n + 2) * (2 + 3) + 18
    return numerator / tot


